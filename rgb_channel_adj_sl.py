import streamlit as st
import numpy as np
from PIL import Image


def adjust_rgb_channels(image, r_factor, g_factor, b_factor):
    # Convert image to float32 and normalize
    img_float = np.array(image).astype(np.float32) / 255.0

    # Adjust RGB channels
    img_float[:, :, 0] *= r_factor
    img_float[:, :, 1] *= g_factor
    img_float[:, :, 2] *= b_factor

    # Clip values to [0, 1] range
    img_float = np.clip(img_float, 0, 1)

    # Convert back to uint8
    return Image.fromarray((img_float * 255).astype(np.uint8))


st.title("RGB Channel Adjuster")

uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    st.write("Adjust RGB channel intensities:")
    r_factor = st.slider("Red", 0.0, 1.0, 1.0, 0.1)
    g_factor = st.slider("Green", 0.0, 1.0, 1.0, 0.1)
    b_factor = st.slider("Blue", 0.0, 1.0, 1.0, 0.1)

    adjusted_image = adjust_rgb_channels(image, r_factor, g_factor, b_factor)
    st.image(adjusted_image, caption="Adjusted Image", use_column_width=True)
else:
    st.write("Please upload an image to begin.")
