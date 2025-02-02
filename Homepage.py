import streamlit as st
#from streamlit_option_menu import option_menu


# ---------- Setup ------------ #

# Setup Page Navigation
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True) # set fonts
lib = st.Page("pages/1_library.py", title="Grimoire",)
meta = st.Page("pages/2_meta.py", title="Strategy Oracle",)
# tier = st.Page("pages/3_tier_list.py", title="Tier List",) # Commented out for testing - Blank page
spin = st.Page("pages/4_spin.py", title="Summoning Ritual",)

# Common Attributes
st.sidebar.markdown("# __Most Credible Source 100 emoji__")
st.sidebar.columns([1,7,0.5])[1].markdown(":violet[ \
    *\"The Magic that gathered as statistics rules the land.... only one may rise against the onslaught of the **Trumpinator***\" \
    ]")

st.html("""
  <style>
    [alt=Logo] {
      height: 3rem;
    }
  </style>
        """) # set size
st.logo(
    image="Data/Logo.png",
    icon_image="Data/circle.png",
    size="large"
)
#st.image('')

# Init Multipage
pg = st.navigation([lib, meta, spin]) # Removed tier from the list
pg.run()








