import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def main():
    st.title("Project 1")
    st.subheader("Professor Malek Adjouadi")
    st.subheader("Student: Luana Sawada & PantherID: 1111111")

    st.write("Enter the desired data")

    st.set_option('deprecation.showfileUploaderEncoding', False)
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        # st.write(uploaded_file)
        image1 = Image.open(uploaded_file)
        # st.image(uploaded_file, caption='Sunrise by the mountains',    use_column_width = True)
        st.image(image1, caption='Image', use_column_width = True)

    black_and_white = st.checkbox("Turn this image into black and white")
    if black_and_white:
        image_file = image1.convert('1')
        st.image(image_file, caption='Image', use_column_width = True)

    option = st.selectbox('Which picture would you like to use as input?',
                        (1, 2, 3, 4))
    st.write('You selected:', option)

if __name__ == '__main__':
    main()