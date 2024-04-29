import streamlit as st
import selector.login_screen as ls
from configure import pagesetup as ps
from configure import stylable as stbl
from display import display_fonts, set_background
from configure.stylable import large_stylable_container_1, additional_content_1

ps.Menu_tabs_display()
ps.MSU_logo()
display_fonts()
# URL of the background image
image_url = "https://raw.githubusercontent.com/jbeduze/MSU-Wrestling/main/.streamlit/config/e52cca5a-1264-4351-ac5e-ad48bd46ea9b.webp"
set_background(image_url)

st.markdown('<p class="cinzel-header">MSU Wrestling</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,1,4])


st.write("Welcome to the wrestling site")

large_stylable_container_1("MSU wrestling", "personal profile", additional_content_1)
