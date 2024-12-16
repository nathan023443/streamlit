

import streamlit as st

# Set the title of the web page
st.title("simple web form with streamlit")
# Set a header
st.header("user information users")
# Text input for name
name= st.text_input('Enter your name')
# Dropdown menu for selecting an option
option=['Hawk Tuah', 'Stillwater' , 'Lunchly']
selected_option= st.selectbox('choose an option', option)
# Slider for selecting a value
slider_value= st.slider('select a value',1, 100, 50)
#radio button for selecting gender
Gender=st.radio('select your gender:', {"Male", 'Female', 'other'})
#checkboxes for hobbies
hobbies=[]
if st.checkbox('reading'):
        hobbies.append('reading')
if st.checkbox('traveling'):
      hobbies.append('traveling')
if st.checkbox('cooking'):
      hobbies.append('cooking')
# Submit button
if st.button('submit'):
    st.write(f'Name: {name}')
    st.write(f'selected option:{selected_option}')
    st.write(f'Slider ValueL {slider_value}')
    st.write(f'Gender: {Gender}')
    st.write(f"hobbies {','.join(hobbies) if hobbies else 'None'} ")
# Additional information
st.subheader('Summary')
st.write('Fill out the form above and click the submit button')
# Footer
