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

output = []
for row in data:
    if row[0] not in output:
        output.append(row[0])
print(output)

for archetypes in output:
    print(archetypes, end=",")
