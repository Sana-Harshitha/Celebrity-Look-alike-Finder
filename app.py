import streamlit as st
import numpy as np
import pandas as pd
import cv2
from PIL import Image
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity
from load_data import load_data

# ------------------ Load Functions ------------------
@st.cache_resource
def load_insightface_app():
    app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
    app.prepare(ctx_id=0)
    return app

@st.cache_data
def load_celeb_data():
    return load_data()

def get_face_embedding(image, app):
    image_rgb = image.convert("RGB")
    img_np = np.array(image_rgb)
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    faces = app.get(img_bgr)
    if len(faces) == 0:
        st.error("No face detected. Please upload a clearer image.")
        return None
    elif len(faces) > 1:
        st.error("Multiple faces detected. Please upload an image with only one person.")
        return None
    else:
        largest_face = max(faces, key=lambda f: (f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))
        return largest_face.embedding

def find_best_match(user_embedding, df):
    celeb_embeddings = np.stack(df['embedding'].values)
    similarities = cosine_similarity([user_embedding], celeb_embeddings)[0]
    best_idx = np.argmax(similarities)
    return df.iloc[best_idx], similarities[best_idx]

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="Celebrity Look-alike", layout="wide")

# Title
st.title("Celebrity Look-alike Finder")
st.markdown("Upload or capture a photo. The app will find the Indian celebrity you resemble the most.")

# Sidebar input
with st.sidebar:
    st.header("Input Photo")
    upload_option = st.radio("Select Image Source", ["Upload", "Camera"])
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"]) if upload_option == "Upload" else st.camera_input("Take a photo")

# Main logic
if uploaded_file:
    image = Image.open(uploaded_file)
    app = load_insightface_app()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Your Image")
        st.image(image, caption="Uploaded Photo", width=300)

    with col2:
        with st.spinner("Analyzing..."):
            user_embedding = get_face_embedding(image, app)

            if user_embedding is not None:
                df = load_celeb_data()
                match, similarity = find_best_match(user_embedding, df)

                st.subheader("Match Result")
                st.write(f"Name: {match['celeb_name']}")
                st.write(f"Similarity Score: {similarity * 100:.2f}%")
            else:
                st.warning("Could not process the image. Ensure it's clear and contains only one face.")
else:
    st.info("Use the sidebar to upload or capture an image to get started.")

# Footer
st.markdown("---")
st.caption("Developed using Streamlit and InsightFace")
