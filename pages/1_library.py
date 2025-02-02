# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:27:10 2025

@author: vince
"""
import streamlit as st
#import streamlit.components as com
import base64
import plotly.express as px
import matplotlib.pyplot as plt

from dataGather import getSingleArchetypeOverallData


# --------- Functions --------- #
def search_library():
    if selected_archetype:
        with search_result:
            
            # Archetype Description
            #st.markdown("---")
            st.markdown(f'# {selected_archetype}')
                #Type
                #Description
            st.markdown('>A Magic Archetype is a recurring deck or strategy with many possible variations. \
                        Archetypes are defined when they have been prevalent in several tournaments and have \
                            showed results repeatedly, Top 8 or higher. They should also be an idea that is playable \
                                in many formats, rather than just a pile of cards that wins.')
            
            # Relevant Stats
            tab1, tab2 = search_result.tabs(["Best Winrate", "All Winrates"])

            with tab1:
                if (getSingleArchetypeOverallData(selected_archetype) == None):
                    win_rate, sample_size, std_dev = ("-", "-", "-")
                else:
                    win_rate, sample_size, std_dev = (getSingleArchetypeOverallData(selected_archetype))
                tab1.markdown(f"## Winrate: {win_rate}%")
                tab1.markdown(f"### Sample size: {sample_size} matches")
            #anim_in(tab1)
            
#def anim_in(tab1):



    
    
    
#@st.cache(allow_output_mutation=True) 
def base64_img(image):
    with open(image, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()



# Data 
archetype_list = ['Izzet Phoenix', 'Azorius Control', 'Rakdos Demons', 'Selesnya Company', 'Enigmatic Incarnation', 'Mono Black Demons', 'Lotus Field Combo', 'Green Devotion', 'Mardu Greasefang', 'Rakdos Midrange', 'Abzan Greasefang', 'Domain Zur', 'Azorius Spirits', '5 Color Niv-Mizzet', 'Azorius Lotus Field', 'Boros Tokens Control', 'Jund Sacrifice', 'Azorius Humans', 'Mono White Humans', 'Rakdos Transmogrify', 'Rakdos Prowess', 'Orzhov Demons', 'Quintorius Combo', 'Boros Burn', 'Dimir Ninjas', 'Esper Control', '5 Color Landfall', 'Mono Black', 'Red Deck Wins', 'Izzet Creativity', 'Goblins', 'Dimir Rogues', 'Dimir Control', 'Boros Heroic', 'Golgari Sacrifice', 'Atarka Red', 'Golgari Midrange', 'Gruul Prowess', 'Jeskai Creativity', 'Boros Creativity', 'Boros Convoke', 'Boros Transmogrify', 'Sultai Ramp', '4 Color Rona', 'Rakdos Creativity', 'Rakdos Cauldron', 'Esper Greasefang', 'Orzhov Tokens', 'Bring to Beanstalk', 'Orzhov Humans', 'Sultai Yorion', 'Jeskai Control', 'Merfolks', 'Bant Spirits', 'Orzhov Midrange', 'Jeskai Ascendancy', 'Mono Blue Spirits', 'Archfiend Alteration', 'Golgari Roots', 'Rainbow Humans', 'Mardu Reanimator', 'Golgari Demons', 'Soulflayer Time', 'Acererak Combo', 'Selesnya Enchantments', 'Metalwork Colossus', 'Mono White Tokens', 'Orzhov Aggro', 'Sultai Rona', 'Sultai Scapeshift', 'Simic Lands', 'Gruul Aggro', 'Dimir Proft', 'Esper Reanimator', 'Ensoul Artifacts', 'Grixis Phoenix', 'Jund Transmogrify', 'Naya Midrange', 'Izzet Prowess', 'Elves', 'Azorius Mentor', 'Temur Company', 'Gruul Vehicles', 'Dimir Midrange', 'Hardened Scales', 'Bring to Light', 'Neoform', 'Jund Citadel', 'Jund Landfall', 'Aclazotz Slasher Combo', 'Orzhov Superfriends', 'Azorius Flash', 'Selesnya Blink', 'Azorius Tempo', 'Rakdos Sacrifice', 'Gruul Bard Class', 'Mardu Doom', 'Mill', 'Mardu Transmogrify', 'Dimir Demons', 'Esper Midrange', 'Storm Herald', '5 Color Superfriends', '4 Color Omnath', 'Boros Vehicles', 'Golgari Citadel', 'Grinning Ignus Combo', 'Bant Humans', 'Mono Blue Jewel', 'Dredgeless Dredge', 'Simic Company', 'Gruul Company', 'Boros Tokens', '4 Color Greasefang', 'Jeskai Mentor', "Thassa's Bargain", 'Azorius Tokens', 'Mardu Virtuoso', '4 Color Zur', 'Azorius Cauldron', 'Mono Green Stompy', 'Azorius Midrange', 'Orzhov Control', 'Jeskai Fires', 'Boros Midrange', '5 Color Yorion', 'Bant Blink', '4 Color Legends', 'Dimir Faeries', 'Orzhov Reanimator', 'Selesnya Kona', 'Azorius Flyers', 'Orzhov Yorion', 'Bant Control', 'Orzhov Waste Not', 'Azorius Helix', 'Mardu Midrange', 'Rakdos Madness', 'Esper Humans', 'Golgari Deathtouch']

img = base64_img("Data/magic_library.jpg")
#Bakcground 
page_bg_img = '''
    <style>
        .stApp {
            background-image: url("https://www.peabodylibrary.org/freeforall/wp-content/uploads/2015/11/141795_library-fantasy-art-books-artwork-4000x2500-wallpaper_www.wall321.com_39.jpg");
            background-size: cover;
            }
        [data-testid="stHeader"] {
            background-color: rgba(0,0,0,0);
            }
        [class="stVerticalBlock st-key-result st-emotion-cache-1atdbe9 eiemyj3"] {
            background-color: rgba(1,1,1,0.5);
            
            }
        [data-testid="stImage"] {
            gap: -5rem;
            }
    </style>
    '''
st.markdown(page_bg_img, unsafe_allow_html=True)
#st.columns(5)[2].image('Data/book2.jpg')

# Search Bar 
selected_archetype = st.selectbox('Search the Grimoire...', archetype_list, index=None, placeholder='Search the Grimoire...', label_visibility='hidden')
tags = st.multiselect('Tags',['blue', 'green', 'red', 'black', 'white'], placeholder="Tags", label_visibility='hidden')

# Search Button
st.columns(5)[2].button('Search', on_click=search_library)

# Search Result
search_result = st.container(key='result')




