import streamlit as st
import requests
from db import save_card, get_all_cards

SCRYFALL_API_URL = "https://api.scryfall.com/cards/search"


def fetch_cards(card_name):
    params = {"q": card_name}
    response = requests.get(SCRYFALL_API_URL, params=params)
    return response.json().get("data", []) if response.status_code == 200 else []


st.title("MTG Card Finder")

card_name = st.text_input("Enter Card Name")

if st.button("Search"):
    cards = fetch_cards(card_name)

    if cards:
        for card in cards:
            st.subheader(card['name'])
            st.image(card.get("image_uris", {}).get("normal", "https://via.placeholder.com/150"))
            st.write(f"Set: {card['set_name']} - Rarity: {card['rarity']}")

            if st.button(f"Save {card['name']}", key=card['id']):
                save_card(card)
                st.success(f"Saved {card['name']} to database!")
    else:
        st.error("No cards found!")

st.sidebar.header("Saved Cards")
saved_cards = get_all_cards()
for card in saved_cards:
    st.sidebar.write(f"- {card['name']} ({card['set_name']})")