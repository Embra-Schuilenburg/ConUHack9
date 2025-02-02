# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:26:50 2025

@author: vince
"""
import streamlit as st
import  streamlit_vertical_slider  as svs
from streamlit_extras.row import row 

col1, col2, col3, col4= st.columns([3, 4, 3, 1], vertical_alignment="center")

#Headers
col1.title('Meta')

col3.title('Decks')
with col3: 
    reccs = st.container()


#data
archetype_list = ['Izzet Phoenix', 'Azorius Control', 'Rakdos Demons', 'Selesnya Company', 'Enigmatic Incarnation', 'Mono Black Demons', 'Lotus Field Combo', 'Green Devotion', 'Mardu Greasefang', 'Rakdos Midrange', 'Abzan Greasefang', 'Domain Zur', 'Azorius Spirits', '5 Color Niv-Mizzet', 'Azorius Lotus Field', 'Boros Tokens Control', 'Jund Sacrifice', 'Azorius Humans', 'Mono White Humans', 'Rakdos Transmogrify', 'Rakdos Prowess', 'Orzhov Demons', 'Quintorius Combo', 'Boros Burn', 'Dimir Ninjas', 'Esper Control', '5 Color Landfall', 'Mono Black', 'Red Deck Wins', 'Izzet Creativity', 'Goblins', 'Dimir Rogues', 'Dimir Control', 'Boros Heroic', 'Golgari Sacrifice', 'Atarka Red', 'Golgari Midrange', 'Gruul Prowess', 'Jeskai Creativity', 'Boros Creativity', 'Boros Convoke', 'Boros Transmogrify', 'Sultai Ramp', '4 Color Rona', 'Rakdos Creativity', 'Rakdos Cauldron', 'Esper Greasefang', 'Orzhov Tokens', 'Bring to Beanstalk', 'Orzhov Humans', 'Sultai Yorion', 'Jeskai Control', 'Merfolks', 'Bant Spirits', 'Orzhov Midrange', 'Jeskai Ascendancy', 'Mono Blue Spirits', 'Archfiend Alteration', 'Golgari Roots', 'Rainbow Humans', 'Mardu Reanimator', 'Golgari Demons', 'Soulflayer Time', 'Acererak Combo', 'Selesnya Enchantments', 'Metalwork Colossus', 'Mono White Tokens', 'Orzhov Aggro', 'Sultai Rona', 'Sultai Scapeshift', 'Simic Lands', 'Gruul Aggro', 'Dimir Proft', 'Esper Reanimator', 'Ensoul Artifacts', 'Grixis Phoenix', 'Jund Transmogrify', 'Naya Midrange', 'Izzet Prowess', 'Elves', 'Azorius Mentor', 'Temur Company', 'Gruul Vehicles', 'Dimir Midrange', 'Hardened Scales', 'Bring to Light', 'Neoform', 'Jund Citadel', 'Jund Landfall', 'Aclazotz Slasher Combo', 'Orzhov Superfriends', 'Azorius Flash', 'Selesnya Blink', 'Azorius Tempo', 'Rakdos Sacrifice', 'Gruul Bard Class', 'Mardu Doom', 'Mill', 'Mardu Transmogrify', 'Dimir Demons', 'Esper Midrange', 'Storm Herald', '5 Color Superfriends', '4 Color Omnath', 'Boros Vehicles', 'Golgari Citadel', 'Grinning Ignus Combo', 'Bant Humans', 'Mono Blue Jewel', 'Dredgeless Dredge', 'Simic Company', 'Gruul Company', 'Boros Tokens', '4 Color Greasefang', 'Jeskai Mentor', "Thassa's Bargain", 'Azorius Tokens', 'Mardu Virtuoso', '4 Color Zur', 'Azorius Cauldron', 'Mono Green Stompy', 'Azorius Midrange', 'Orzhov Control', 'Jeskai Fires', 'Boros Midrange', '5 Color Yorion', 'Bant Blink', '4 Color Legends', 'Dimir Faeries', 'Orzhov Reanimator', 'Selesnya Kona', 'Azorius Flyers', 'Orzhov Yorion', 'Bant Control', 'Orzhov Waste Not', 'Azorius Helix', 'Mardu Midrange', 'Rakdos Madness', 'Esper Humans', 'Golgari Deathtouch']

#fields
opp1 = col1.selectbox('First Opponent', archetype_list, index=None, placeholder='First Opponent', label_visibility='hidden')
opp2 = col1.selectbox('Second Opponent', archetype_list, index=None, placeholder='Second Opponent', label_visibility='hidden')
opp3 = col1.selectbox('Third Opponent', archetype_list, index=None, placeholder='Third Opponent', label_visibility='hidden')
opp4 = col1.selectbox('Fourth Opponent', archetype_list, index=None, placeholder='Fourth Opponent', label_visibility='hidden')
opp5 = col1.selectbox('Fifth Opponent', archetype_list, index=None, placeholder='Fifth Opponent', label_visibility='hidden')

#Recommend

def recommend():
    print("touch grass")
    reccs.text("lorew ipsum" *10)


col2.vertical_alignment = "center"
col2.button('Calculate', on_click=recommend())


with col4:
    row1 = row(2, vertical_align="center")
    svs.vertical_slider(key='vertical', 
                    default_value=0, 
                    step=1, 
                    min_value=0, 
                    max_value=100,
                    slider_color= ('red', 'blue'), #optional
                    track_color='lightgrey', #optional
                    thumb_color = 'black', #optional
                    )





