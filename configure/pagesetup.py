import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from tabs import main, personal_stats, personalized_plans, profile, team, ai_chat_and_upload, coach
from configure import stylable as styl


#display msu Wrestling on app.py
def Header_display():
    # Inject custom CSS
    css_style = """
    <style>
        .cinzel-header {
            position: absolute;  # Absolute positioning
            top: 100px;          # 100px from the top of the viewport
            left: 60%;           # Horizontally centered
            transform: translateX(-50%);  # Ensure it's perfectly centered
            font-size: 24px;     # Font size
            color: #4a4a4a;      # Font color
        }
    </style>
    """




def Menu_tabs_display():
    """Creates tabs for the Streamlit app for different sections with custom CSS for positioning."""
    # Inject custom CSS to move the tabs higher and adjust styling
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Cinzel&display=swap');

            /* Apply the Cinzel font to the Streamlit tabs */
            .stTabs > div > button {
                font-family: 'Cinzel', serif;
                font-size: 100px;  /* Adjust font size as needed */
                color: #444;  /* Adjust font color as needed */
            /* Reduce the space at the top of the page */
            .css-18e3th9 {
                padding-top: 0rem !important;
            }
            /* Additional styling for tabs */
            .stTabs {
                margin-top: -3.5rem;  /* Move tabs up */
            }
        </style>
        """, unsafe_allow_html=True)

    with st.container():
        tabs = st.tabs(["Main", "Personal Stats", "Personalized Plans", "Profile", "Team", "AI Chat and Upload", "Coach"])
        pages = [main, personal_stats, personalized_plans, profile, team, ai_chat_and_upload, coach]

        for tab, page in zip(tabs, pages):
            with tab:
                page.show()

import streamlit as st
import os  # Import os to check file existence

def umich_mascot():
    """Displays the umich mascot in the upper left corner of the page with custom CSS."""
    # Local path to the PNG file
    local_image_path = "https://github.com/jbeduze/MSU-Wrestling/blob/main/Wolverine_single.png"  # Change this to the path of your local file

    # Check if the file exists
    if not os.path.exists(local_image_path):
        st.error(f"File not found: {local_image_path}")
        return  # Exit the function if file is not found

    # Inject custom CSS to move the image slightly down and to the right
    st.markdown("""
        <style>
            .logo-container {
                position: fixed;
                top: 10px;  /* Adjusted down by 10px */
                left: 10px;  /* Adjusted right by 10px */
                z-index: 999;  /* Ensure logo is on top of other content */
            }
        </style>
        <div class="logo-container">
            <img src="{}" alt="MSU Logo" style="width: 100px; height: auto;">
        </div>
        """.format(local_image_path), unsafe_allow_html=True)


