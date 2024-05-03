import streamlit as st
from configure.stylable import large_stylable_container_1, additional_content_1, large_stylable_container_2, additional_content_2

def show():
    st.header("Profile")
    st.write("Content for Profile here.")
    # Add more widgets and functionality specific to the Personal Stats page

    large_stylable_container_1 ("Athlete Stat.s", "win/lose records", additional_content_1)

    large_stylable_container_2 ("diet and workout summary", "current goal", additional_content_2)