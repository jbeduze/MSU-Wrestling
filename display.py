import streamlit as st
import base64


#fonts
def local_css(file_name):
    path = f"configure/{file_name}"
    with open(path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def display_fonts():
    # Load the local CSS file
    local_css("style.css")

    # Streamlit elements using the styles
    # st.title('Welcome to My App')  # This will use Cinzel by default from CSS
    # st.header('This is a header')  # This will also use Cinzel
    # st.subheader('This is a subheader')  # Adjust in CSS if you want this in Cinzel
    # st.write('This is regular text content.')  # This will use Forum

#background image
def set_background(url):
    """
    Set the background of the Streamlit app to the given image URL.
    """
    # CSS to inject contained in a string
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("{url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """

    # Inject CSS with Markdown
    st.markdown(background_style, unsafe_allow_html=True)

def set_background_1():
    """
    Set the background of the Streamlit app using a locally stored image.
    """
    image_path = 'configure/msuhelmet.png'  # Update this path
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """

    st.markdown(background_style, unsafe_allow_html=True)

def hide_streamlit_header():
    """
    Hide the Streamlit header and menu button.
    """
    hide_header_style = """
        <style>
            header[data-testid="stHeader"] {
                display: none;
            }
        </style>
        """
    st.markdown(hide_header_style, unsafe_allow_html=True)