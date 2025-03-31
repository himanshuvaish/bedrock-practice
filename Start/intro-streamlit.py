# Streamlit is an open-source Python framework for building front-end applications to demo machine learning 
# applications. Streamlit provides a library of commands for displaying web elements. 
# You can see the list of controls in the Streamlit API reference .

# Streamlit allows you to build simple and attractive user interfaces with a relatively small amount of Python code.
#  For back-end developers, this means you can create demo applications for your code, without having to learn the various 
# programming languages, frameworks, and hosting platforms for front-end development. Even for front-end developers,
#  it allows you to quickly build a proof of concept to validate your approach.

# Streamlit is well suited for creating generative AI prototypes. 
# Throughout this workshop, you will have the opportunity to try a wide variety of
#  Streamlit's capabilities that greatly simplify the demo-building process.

import streamlit as st #all streamlit commands will be available through the "st" alias

st.set_page_config(page_title="Streamlit Demo") #HTML title
st.title("Streamlit Demo") #page title

color_text = st.text_input("What's your favorite color?") #display a text box
go_button = st.button("Go", type="primary") #display a primary button

if go_button: #code in this if block will be run when the button is clicked

    st.write(f"I like {color_text} too!") #display the response content
