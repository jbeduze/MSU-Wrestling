import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def set_title(varTitle, varSubtitle):
    # Define CSS styles for container and markdown within it
    container_styles = """
        {
            border: 1px solid rgba(115, 0, 0, 1);
            background-color: rgba(115, 0, 0, 0.75);
        }
    """
    markdown_styles = """
        .stMarkdown {
            padding-right: 0.2em;
            padding-left: 0.5em;
        }
    """
    # Apply styles to container and display the subtitle
    with stylable_container(key="container_with_border", css_styles=[container_styles, markdown_styles]):
        st.markdown(f"<span style='font-weight: bold; color:#0096D7; font-size:1.3em;'>{varSubtitle}</span>", unsafe_allow_html=True)
        st.divider()

# Background image URL
bg_image_url = "https://raw.githubusercontent.com/jbeduze/MSU-Wrestling/main/.streamlit/config/e52cca5a-1264-4351-ac5e-ad48bd46ea9b.webp"

# CSS string to set background image
bg_style = f"""
<style>
    body {{
        background-image: url("{bg_image_url}");
        background-size: cover;
    }}
</style>
"""

# Inject CSS to set the background image
st.markdown(bg_style, unsafe_allow_html=True)
