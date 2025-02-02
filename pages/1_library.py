# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:27:10 2025

@author: vince
"""
import streamlit as st
import streamlit.components as com

# --------- Functions --------- #
def search_library():
    if selected_archetype:
        with search_result:
            st.markdown("---")
            st.write(f'{selected_archetype}')
            
def anim_in():
    return 0

# Data 
archetype_list = ['Izzet Phoenix', 'Azorius Control', 'Rakdos Demons', 'Selesnya Company', 'Enigmatic Incarnation', 'Mono Black Demons', 'Lotus Field Combo', 'Green Devotion', 'Mardu Greasefang', 'Rakdos Midrange', 'Abzan Greasefang', 'Domain Zur', 'Azorius Spirits', '5 Color Niv-Mizzet', 'Azorius Lotus Field', 'Boros Tokens Control', 'Jund Sacrifice', 'Azorius Humans', 'Mono White Humans', 'Rakdos Transmogrify', 'Rakdos Prowess', 'Orzhov Demons', 'Quintorius Combo', 'Boros Burn', 'Dimir Ninjas', 'Esper Control', '5 Color Landfall', 'Mono Black', 'Red Deck Wins', 'Izzet Creativity', 'Goblins', 'Dimir Rogues', 'Dimir Control', 'Boros Heroic', 'Golgari Sacrifice', 'Atarka Red', 'Golgari Midrange', 'Gruul Prowess', 'Jeskai Creativity', 'Boros Creativity', 'Boros Convoke', 'Boros Transmogrify', 'Sultai Ramp', '4 Color Rona', 'Rakdos Creativity', 'Rakdos Cauldron', 'Esper Greasefang', 'Orzhov Tokens', 'Bring to Beanstalk', 'Orzhov Humans', 'Sultai Yorion', 'Jeskai Control', 'Merfolks', 'Bant Spirits', 'Orzhov Midrange', 'Jeskai Ascendancy', 'Mono Blue Spirits', 'Archfiend Alteration', 'Golgari Roots', 'Rainbow Humans', 'Mardu Reanimator', 'Golgari Demons', 'Soulflayer Time', 'Acererak Combo', 'Selesnya Enchantments', 'Metalwork Colossus', 'Mono White Tokens', 'Orzhov Aggro', 'Sultai Rona', 'Sultai Scapeshift', 'Simic Lands', 'Gruul Aggro', 'Dimir Proft', 'Esper Reanimator', 'Ensoul Artifacts', 'Grixis Phoenix', 'Jund Transmogrify', 'Naya Midrange', 'Izzet Prowess', 'Elves', 'Azorius Mentor', 'Temur Company', 'Gruul Vehicles', 'Dimir Midrange', 'Hardened Scales', 'Bring to Light', 'Neoform', 'Jund Citadel', 'Jund Landfall', 'Aclazotz Slasher Combo', 'Orzhov Superfriends', 'Azorius Flash', 'Selesnya Blink', 'Azorius Tempo', 'Rakdos Sacrifice', 'Gruul Bard Class', 'Mardu Doom', 'Mill', 'Mardu Transmogrify', 'Dimir Demons', 'Esper Midrange', 'Storm Herald', '5 Color Superfriends', '4 Color Omnath', 'Boros Vehicles', 'Golgari Citadel', 'Grinning Ignus Combo', 'Bant Humans', 'Mono Blue Jewel', 'Dredgeless Dredge', 'Simic Company', 'Gruul Company', 'Boros Tokens', '4 Color Greasefang', 'Jeskai Mentor', "Thassa's Bargain", 'Azorius Tokens', 'Mardu Virtuoso', '4 Color Zur', 'Azorius Cauldron', 'Mono Green Stompy', 'Azorius Midrange', 'Orzhov Control', 'Jeskai Fires', 'Boros Midrange', '5 Color Yorion', 'Bant Blink', '4 Color Legends', 'Dimir Faeries', 'Orzhov Reanimator', 'Selesnya Kona', 'Azorius Flyers', 'Orzhov Yorion', 'Bant Control', 'Orzhov Waste Not', 'Azorius Helix', 'Mardu Midrange', 'Rakdos Madness', 'Esper Humans', 'Golgari Deathtouch']


# Search Bar 
selected_archetype = st.selectbox('Search the Grimoire...', archetype_list, index=None, placeholder='Search the Grimoire...', label_visibility='hidden')
tags = st.multiselect('Tags',['blue', 'green', 'red', 'black', 'white'], placeholder="Tags", label_visibility='hidden')

# Search Button
st.columns(5)[2].button('Search', on_click=search_library)

# Search Result
search_result = st.container()



