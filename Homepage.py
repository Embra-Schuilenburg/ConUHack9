import streamlit as st
#from streamlit_option_menu import option_menu


# ---------- Setup ------------ #

# Setup Page Navigation
lib = st.Page("pages/1_library.py", title="Grimoire",)
meta = st.Page("pages/2_meta.py", title="Strategy Oracle",)
tier = st.Page("pages/3_tier_list.py", title="Tier List",)
spin = st.Page("pages/4_spin.py", title="Summoning Ritual",)

# Common Attributes
st.sidebar.title("Most Credible Source 100 emoji")
st.sidebar.markdown(":blue[*The Magic that gathered as statistics rules the land.... only one may rise against the onslaught of the **Trumpinator***]")
st.logo(
    image="Data/circle.png",
    icon_image="Data/circle.png",
    size="large"
)

# Init Multipage
pg = st.navigation([lib, meta, tier, spin])
pg.run()








