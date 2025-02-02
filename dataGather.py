# import requests
# from bs4 import BeautifulSoup
#
#
# # Making a GET request
# # r = requests.get('https://mtgdecks.net/Pioneer/winrates')
#
# # check status code for response received
# # success code - 200
# # print(r)
#
# # Parsing the HTML
# soup = BeautifulSoup(open("archetypeData.html"), features="html.parser")
# #print(soup.prettify())
#
# # On the site all archetype data is in winrate-cell tds and then stored in data divs
# s = soup.find('td', class_='winrate-cell')
# content = soup.find_all('div', class_='data')
#
# #print(content)
#
# # import webdriver
# from selenium import webdriver
#
# # create webdriver object
# driver = webdriver.Firefox()
#
# # get google.co.in
# driver.get("https://google.co.in / search?q = mtg decks pioneer winrates")

archetypes = "Izzet Phoenix, Azorius Control, Rakdos Demons, Selesnya Company, Enigmatic Incarnation, Mono Black Demons, Lotus Field Combo, Green Devotion, Mardu Greasefang, Rakdos Midrange, Abzan Greasefang, Domain Zur, Azorius Spirits, 5 Color Niv-Mizzet, Azorius Lotus Field, Boros Tokens Control, Jund Sacrifice, Azorius Humans, Mono White Humans, Rakdos Transmogrify, Rakdos Prowess, Orzhov Demons, Quintorius Combo, Boros Burn, Dimir Ninjas, Esper Control, 5 Color Landfall, Mono Black, Red Deck Wins, Izzet Creativity, Atarka Red, Golgari Midrange"
izPh = ""
archetypes = archetypes.replace(" \t", ", ")
#print(archetypes)

import csv

with open('Data/statsCleaned.csv', newline='\n') as csvfile:
    # data is read from the relative CSV containing match data, first row of the list contains column headers.
    # The 0th element of the row-0 is empty to respect that the 0th column stores the deck archetypes players can
    # select from. NOTE: There are more user selection options (120) than meta options (32)
    data = list(csv.reader(csvfile))

print(data[4][0])
