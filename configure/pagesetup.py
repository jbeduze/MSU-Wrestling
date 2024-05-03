import streamlit as st
import base64
import os
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
            font-size: 20px;     # Font size
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
                font-size: 120px;  /* Adjust font size as needed */
                color: #444;  /* Adjust font color as needed */
            /* Reduce the space at the top of the page */
            .css-18e3th9 {
                padding-top: 0rem !important;
            }
            /* Additional styling for tabs */
            .stTabs {
                margin-top: -7rem;  /* Move tabs up */
            }
        </style>
        """, unsafe_allow_html=True)
    with st.container():
        tabs = st.tabs(["Main", "Personal Stats", "Personalized Plans", "Profile", "Team", "AI Chat and Upload", "Coach"])
        pages = [main, personal_stats, personalized_plans, profile, team, ai_chat_and_upload, coach]

        for tab in zip(tabs):
            with tab:
                tab.show()



# def umich_mascot():
#     """Displays the umich mascot in the desired position with custom CSS."""
#     local_image_path = "configure/fwolverine.png"
#     if os.path.exists(local_image_path):
#         # Inject custom CSS to precisely position the image
#         st.markdown(f"""
#             <style>
#                 .fixed-logo {
#                     top: -10px;        /* Move image up */
#                     left: -10px;       /* Move image to the left */
#                     z-index: 999;      /* Ensure logo is above other content */
#                 }
#                 /* Additional style to prevent interactions */
#                 .fixed-logo img {
#                     pointer-events: none;  /* Makes the image non-interactive */
#                 }
#             </style>
#             <div class="fixed-logo">
#                 <img src="{local_image_path}" alt="UMich Logo" style="width: 500px; height: auto;">
#             </div>
#             """, unsafe_allow_html=True)







