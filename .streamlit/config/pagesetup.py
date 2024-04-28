import streamlit as st
from streamlit_extras.stylable_container import stylable_container


def set_title(varTitle, varSubtitle):
        with stylable_container(
                key="container_with_border",
                css_styles=["""
                    {
                        border: 1px solid rgba(115, 0, 0, 1);
                        background-color: rgba(115, 0, 0, .75);
                       
                        
                    }
                    """,
                    """
                    .stMarkdown {
                            padding-right: .2em;
                            padding-left: .5em;
                        """]
                ):
                        st.markdown(f"""<span style="font-weight: bold; color:#0096D7; font-size:1.3em;">{varSubtitle}</span>""", unsafe_allow_html=True)
                        st.divider()







#Set Background Image
def display_background_image():
    # Set the Streamlit image for branding as the background with transparency
    background_image = 'https://storage.googleapis.com/production-domaincom-v1-0-8/048/1724048/4RBifvGs/dfc737c8f0d640cfa7e8623583bfcf5e'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.90)), url({background_image});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
