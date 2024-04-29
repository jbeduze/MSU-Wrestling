import streamlit as st


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
