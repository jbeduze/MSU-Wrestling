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

# URL of the image
bg_image_url = "https://raw.githubusercontent.com/jbeduze/MSU-Wrestling/main/.streamlit/config/e52cca5a-1264-4351-ac5e-ad48bd46ea9b.webp
"

# CSS to inject contained in a string
bg_style = f"""
<style>
body {{
background-image: url("{bg_image_url}");
background-size: cover;
}}
</style>
"""

# Inject CSS with Markdown
st.markdown(bg_style, unsafe_allow_html=True)
