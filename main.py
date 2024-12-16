

import streamlit as st

# Set the title of the web page
st.title("simple web form with streamlit")

# Set a header
st.header("user information users")
# Text input for name
name= st.text_input('Enter your name')
# Dropdown menu for selecting an option
option=['option 1', 'option 2' , 'option 3']
selected_option= st.selectbox('choose an option', option)
# Slider for selecting a value
slider_value= st.slider('select a value',1, 100, 1000)

# Submit button
if st.button('submit'):
    st.write(f'Name: {name}')
    st.write(f'selected option:{selected_option}')
    st.write(f'Slider ValueL {slider_value}')
# Additional information
st.subheader('Summary')
st.write('Fill out the form above and click the submit button')
# Footer
