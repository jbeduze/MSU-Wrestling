import streamlit as st
from configure import pagesetup as ps
from configure import stylable as stbl
from display import display_fonts, set_background, set_background_1, hide_streamlit_header, Header_display
from configure.stylable import large_stylable_container_1, additional_content_1

st.set_page_config(page_title="MSU Wrestling", page_icon="🧊", layout="wide")
hide_streamlit_header()
set_background_1()
ps.MSU_logo()
Header_display()
display_fonts()
ps.Menu_tabs_display()

st.write("Welcome to the wrestling site")

large_stylable_container_1("MSU wrestling", "personal profile", additional_content_1)
