import streamlit as st
import requests
from db import *
from analysis import *
from http.server import HTTPServer, BaseHTTPRequestHandler


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
saved_cards = get_all_archetypes()
for card in saved_cards:
    st.sidebar.write(f"- {card['name']} ({card['set_name']})")

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
       if self.path == '/':
           self.path = '/test.html'
       try:
           file_to_open = open(self.path[1:]).read()
           self.send_response(200)
       except:
           file_to_open = "File not found"
           self.send_response(404)
       self.end_headers()
       self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost',8080),Serv)
httpd.serve_forever()