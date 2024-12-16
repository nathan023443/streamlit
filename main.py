import streamlit as st
st.write('yes king')

st.title("are we deaduzz?")
st.header("MANGO MANGO MANGO")
st.subheader("Spit on that thang")

import streamlit as st

# Set the title of the web page
st.title("simple web form with streamlit")

# Set a header
st.header("user information users")
# Text input for name
name= st.text_input('Enter your name')
# Dropdown menu for selecting an option

# Slider for selecting a value
option=['option 1', 'option 2' , 'option 3']
selected_option= st.selections('choose an option', option)
# Submit button
if st.button('submit'):
    st.write(f'Name: {name}')

# Additional information

# Footer
