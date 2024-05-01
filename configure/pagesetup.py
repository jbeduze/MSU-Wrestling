import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from tabs import main, personal_stats, personalized_plans, profile, team, ai_chat_and_upload, coach
from configure import stylable as styl


#MSU white logo display (local)
def MSU_logo():
    """Displays the MSU logo in the upper left corner of the page with custom CSS."""
    # Inject custom CSS to move the image higher and to the right
    st.markdown("""
        <style>
            .logo-container {
                position: fixed;
                top: 0;  /* Adjust as needed to position higher */
                left: 0;  /* Keep logo on the left */
                z-index: 999;  /* Ensure logo is on top of other content */
            }
        </style>
        <div class="logo-container">
            <img src="https://dxbhsrqyrr690.cloudfront.net/sidearm.nextgen.sites/msuspartans.com/images/responsive/main_logo_white.svg" alt="MSU Logo" style="width: 100px; height: auto;">
        </div>
        """, unsafe_allow_html=True)



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
