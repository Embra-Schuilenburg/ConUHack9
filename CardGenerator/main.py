import json
import textwrap
import urllib.request
import requests
from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()


def get_trump_quote() -> str:
    """
    Fetch a random quote from the Trump API.

    Returns:
        A quote string if successful, or an error message.
    """
    url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("message", "No message found.")
    except requests.RequestException as e:
        return f"Error: {e}"


def generate_card_json(quote: str) -> dict:
    """
    Generate a Magic: The Gathering card as JSON using the OpenAI chat API based on a provided quote.

    Args:
        quote: A string containing a Donald Trump quote.

    Returns:
        A dictionary containing card details.
    """
    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI responsible for generating new Magic the Gathering Cards. "
                "The user will only provide you a quote from Donald Trump to base the card around. "
                "Using the quote, provide the following items in a JSON format: "
                "'name', 'mana_cost', 'supertype', 'type', 'abilities', "
                "'flavor', 'power', 'toughness'. If power and toughness are 0 or blank,"
                "Return None for either value as required."
            ),
        },
        {"role": "user", "content": quote},
    ]
    card_response = client.chat.completions.create(
        model="gpt-4o", messages=messages, response_format={"type": "json_object"}
    )
    card_json = card_response.choices[0].message.content
    card_data = json.loads(card_json)

    # Ensure the abilities field is a list of strings
    abilities = card_data.get("abilities")
    if isinstance(abilities, dict):
        card_data["abilities"] = [str(value) for value in abilities.values()]
    elif not isinstance(abilities, list):
        card_data["abilities"] = [str(abilities)]

    return card_data


def generate_card_art(card_data: dict) -> str:
    """
    Generate artwork for the Magic: The Gathering card using the OpenAI image API.

    Args:
        card_data: A dictionary containing card details.

    Returns:
        The filename of the downloaded card artwork.
    """
    image_prompt = (
        f"A Magic: The Gathering card illustration of {card_data['name']}, a {card_data['type']}. "
        "The artwork is highly detailed, fantasy-themed, and features dramatic lighting."
        "Only include the artwork. Do not include the card name. Do not include border in the illustration."
        "Avoid placing details of the image within 100 pixels of the border."
        "Place main details in the center of the image."
    )
    image_response = client.images.generate(
        model="dall-e-2", prompt=image_prompt, size="1024x1024", n=1
    )
    image_url = image_response.data[0].url
    image_filename = "card_art.jpg"
    urllib.request.urlretrieve(image_url, image_filename)
    return image_filename


def crop_image(input_path: str, output_path: str, target_size=(820, 605)) -> None:
    """
    Crop the input image to the target size and save it.

    Args:
        input_path: The file path of the input image.
        output_path: The file path where the cropped image will be saved.
        target_size: A tuple (width, height) for the cropped image size.
    """
    with Image.open(input_path) as img:
        width, height = img.size
        left = (width - target_size[0]) / 2
        top = (height - target_size[1]) / 2
        right = (width + target_size[0]) / 2
        bottom = (height + target_size[1]) / 2
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)
    print(f"Cropped image saved to {output_path}")


def create_final_card(card_data: dict, cropped_art_path: str, blank_card_path: str = "blankcard.jpg") -> str:
    """
    Compose the final Magic: The Gathering card by overlaying artwork and drawing text on a blank card template.

    Args:
        card_data: A dictionary containing card details.
        cropped_art_path: The file path of the cropped artwork.
        blank_card_path: The file path of the blank card template.

    Returns:
        The filename of the final card image.
    """
    card = Image.open(blank_card_path)
    draw = ImageDraw.Draw(card)

    # Paste the artwork onto the card template.
    art_image = Image.open(cropped_art_path)
    art_position = (90, 170)  # Adjust based on the blank card template
    card.paste(art_image, art_position)

    # Define font paths (update these paths if necessary).
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    small_font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    # Load fonts.
    name_font = ImageFont.truetype(font_path, 35)
    mana_font = ImageFont.truetype(font_path, 35)
    type_font = ImageFont.truetype(font_path, 30)
    text_font = ImageFont.truetype(small_font_path, 25)
    power_toughness_font = ImageFont.truetype(font_path, 40)

    # Define text positions.
    name_position = (95, 92)
    mana_position = (912, 92)
    type_position = (95, 805)
    text_box_position = (85, 882)  # top-left position for the abilities/flavor text box
    power_toughness_position = (905, 1200)

    # Draw the card name.
    draw.text(name_position, card_data["name"], fill="black", font=name_font)

    # Draw mana cost, right-aligning it.
    mana_text = card_data["mana_cost"]
    mana_text_length = draw.textlength(mana_text, font=mana_font)
    draw.text((mana_position[0] - mana_text_length, mana_position[1]), mana_text, fill="black", font=mana_font)

    # Draw card type (supertype and type).
    card_type = f"{card_data['supertype']} - {card_data['type']}"
    draw.text(type_position, card_type, fill="black", font=type_font)

    # Wrap and draw abilities and flavor text.
    abilities_text = "\n\n".join(textwrap.fill(ability, width=60) for ability in card_data["abilities"])
    flavor_text = textwrap.fill(card_data["flavor"], width=50)
    combined_text = f"{abilities_text}\n\n{flavor_text}"
    draw.multiline_text(text_box_position, combined_text, fill="black", font=text_font, spacing=4)

    # Draw power/toughness, right-aligning the text.
    pt_text = f"{card_data['power']}/{card_data['toughness']}"
    pt_text_length = draw.textlength(pt_text, font=power_toughness_font)
    draw.text((power_toughness_position[0] - pt_text_length, power_toughness_position[1]),
              pt_text, fill="black", font=power_toughness_font)

    # Save the completed card image.
    safe_name = card_data["name"].replace(" ", "_")
    output_filename = f"final_card_{safe_name}.jpg"
    card.save(output_filename)
    print(f"Card saved to {output_filename}")
    return output_filename


def main():
    # 1. Get a random Trump quote.
    quote = get_trump_quote()
    print("Trump Quote:", quote)

    # 2. Generate the card JSON using the quote.
    card_data = generate_card_json(quote)

    # 3. Generate artwork for the card.
    art_filename = generate_card_art(card_data)

    # 4. Crop the generated artwork.
    cropped_art_filename = "cropped_card_art.jpg"
    crop_image(art_filename, cropped_art_filename)

    # 5. Compose the final card image.
    create_final_card(card_data, cropped_art_filename)


if __name__ == "__main__":
    main()

