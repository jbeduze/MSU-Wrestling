import streamlit as st
import os
from configure import pagesetup as ps
import display as dp
from configure import stylable as stbl
from display import display_fonts, set_background, set_background_1, hide_streamlit_header, Header_display
from configure.stylable import large_stylable_container_1, additional_content_1

st.set_page_config(page_title="University of Michigan - Wrestling", page_icon="🧊", layout="wide")
set_background_1()
# ps.umich_mascot()
Header_display()
display_fonts()
ps.Menu_tabs_display()
# dp.main()


large_stylable_container_1("University of michigan - wrestling", "personal profile", additional_content_1)

