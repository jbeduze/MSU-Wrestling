import streamlit as st

def large_stylable_container_1(varTitle, varSubtitle, content):
    """Create a stylable container with a title, subtitle, and custom content.
    
    Args:
        varTitle (str): The title to be displayed at the top of the container.
        varSubtitle (str): The subtitle to be displayed under the title.
        content (callable): A function that defines additional content inside the container.
    """
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            with st.container():
                st.markdown(f"""
                    <style>
                        .container {{
                            border: 2px solid #E6E8FA;  /* Darker egg shell border */
                            background-color: rgba(255, 255, 240, 0.75);  /* Off white and mostly transparent background */
                            width: 100%;
                            height: 200%;  /* Twice as long */
                            padding: 10px;
                        }}
                        .title {{
                            font-weight: bold;
                            color: #1C453B;
                            font-size: 1.3em;
                            margin-bottom: 0.3em;
                        }}
                        .subtitle {{
                            font-weight: bold;
                            color: #1C453B;
                            font-size: 1em;
                            margin-bottom: 1em;
                        }}
                    </style>
                    <div class="container">
                        <div class="title">{varTitle}</div>
                        <div class="subtitle">{varSubtitle}</div>
                    </div>
                """, unsafe_allow_html=True)
                content()

def additional_content_1():
    # Example function to define what goes inside the container
    st.write("")

def large_stylable_container_2(varTitle, varSubtitle, content):
    """Create a stylable container with a title, subtitle, and custom content.
    
    Args:
        varTitle (str): The title to be displayed at the top of the container.
        varSubtitle (str): The subtitle to be displayed under the title.
        content (callable): A function that defines additional content inside the container.
    """
    with st.container():
        st.markdown(f"""
            <style>
                .container {{
                    border: 2px solid #fffff;  /* Darker egg shell border */
                    background-color: rgba(255, 255, 240, 0.75);  /* Off white and mostly transparent background */
                    width: 100%;
                    height: 200%;  /* Twice as long */
                    padding: 10px;
                }}
                .title {{
                    font-weight: bold;
                    color: #0096D7;
                    font-size: 1.3em;
                    margin-bottom: 0.3em;
                }}
                .subtitle {{
                    font-weight: bold;
                    color: #0096D7;
                    font-size: 1em;
                    margin-bottom: 1em;
                }}
            </style>
            <div class="container">
                <div class="title">{varTitle}</div>
                <div class="subtitle">{varSubtitle}</div>
            </div>
        """, unsafe_allow_html=True)
        content()
def additional_content_2():
    # Example function to define what goes inside the container
    st.write("")