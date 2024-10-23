import streamlit as st
import numpy as np
from PIL import Image


def blend_images(image1, image2, weight1, weight2):
    # Convert images to float32 and normalize
    img1_float = np.array(image1).astype(np.float32) / 255.0
    img2_float = np.array(image2).astype(np.float32) / 255.0

    # Ensure both images have the same shape
    if img1_float.shape != img2_float.shape:
        # Resize image2 to match image1
        image2 = image2.resize(image1.size)
        img2_float = np.array(image2).astype(np.float32) / 255.0

    # Blend images
    blended = weight1 * img1_float + weight2 * img2_float

    # Clip values to [0, 1] range
    blended = np.clip(blended, 0, 1)

    # Convert back to uint8
    return Image.fromarray((blended * 255).astype(np.uint8))

st.title("Image Blender")

col1, col2 = st.columns(2)

with col1:
    uploaded_file1 = st.file_uploader(
        "Choose first image...", type=["jpg", "jpeg", "png"])

with col2:
    uploaded_file2 = st.file_uploader(
        "Choose second image...", type=["jpg", "jpeg", "png"])

if uploaded_file1 is not None and uploaded_file2 is not None:
    image1 = Image.open(uploaded_file1)
    image2 = Image.open(uploaded_file2)

    st.write("Original Images:")
    st.image([image1, image2], caption=["Image 1", "Image 2"], width=300)

    st.write("Adjust blending strengths:")
    weight1 = st.slider("Image 1 Strength", 0.0, 1.0, 0.5, 0.01)
    weight2 = st.slider("Image 2 Strength", 0.0, 1.0, 0.5, 0.01)

    blended_image = blend_images(image1, image2, weight1, weight2)
    st.write("Blended Image:")
    st.image(blended_image, caption="Blended Image", use_column_width=True)
else:
    st.write("Please upload both images to begin blending.")
