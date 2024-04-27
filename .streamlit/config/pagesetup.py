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
