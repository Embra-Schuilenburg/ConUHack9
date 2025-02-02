# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:27:37 2025

@author: vince
"""
import streamlit as st
from st_clickable_images import clickable_images
from st_click_detector import click_detector
import time

col1, col2, col3 = st.columns([3,3,3], vertical_alignment="top")

pack = """
    <a href='#' id='Pack'><img width='30%' src='https://media.wizards.com/2022/images/daily/GoldenPack_475x265.png'></a>
    <style>
    img {
        cursor: pointer;
        transition: all .2s ease-in-out;
    }
    img:hover {
        transform: scale(1.1);
    }
    </style>
    """
clicked = click_detector(pack)


if clicked:
    animation = st.image('Data/summon.gif')
    
    time.sleep(0.8)
    animation.empty()
    
    #get card
    

#col2.image('https://media.wizards.com/2022/images/daily/GoldenPack_475x265.png')