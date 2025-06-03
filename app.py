import streamlit as st
import numpy as np
import pandas as pd
import cv2
from PIL import Image
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity
from load_data import load_data  # assumes this loads a DataFrame with 'celeb_name', 'embedding', 'desc', 'wikipedia_link'

# ---------------------------------------
# Cached: Load InsightFace FaceAnalysis
# ---------------------------------------
@st.cache_resource
def load_insightface_app():
    app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
    app.prepare(ctx_id=0)  # CPU ctx
    return app

# ---------------------------------------
# Cached: Load celebrity embeddings
# ---------------------------------------
@st.cache_data
def load_celeb_data():
    return load_data()  # should return DataFrame with 'celeb_name', 'embedding' (np.array), 'desc', 'wikipedia_link'

# ---------------------------------------
# Get embedding from uploaded image
# ---------------------------------------
def get_face_embedding(image, app):
    """
    Detects and returns the embedding of the largest face in the image using InsightFace.
    Returns None if no or multiple faces are found.
    """
    image_rgb = image.convert("RGB")
    img_np = np.array(image_rgb)
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    faces = app.get(img_bgr)

    if len(faces) == 0:
        st.error("❌ No face detected. Please upload a clearer image.")
        return None
    elif len(faces) > 1:
        st.error("⚠️ Multiple faces detected. Please upload an image with only one person.")
        return None
    else:
        # Return embedding of the largest face
        largest_face = max(faces, key=lambda f: (f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))
        return largest_face.embedding

# ---------------------------------------
# Find closest celebrity match
# ---------------------------------------
def find_best_match(user_embedding, df):
    celeb_embeddings = np.stack(df['embedding'].values)
    similarities = cosine_similarity([user_embedding], celeb_embeddings)[0]
    best_idx = np.argmax(similarities)
    return df.iloc[best_idx], similarities[best_idx]

# ---------------------------------------
# Streamlit UI
# ---------------------------------------
st.set_page_config(page_title="🎭 Celebrity Look-alike Finder", layout="centered")
st.title("🎭 Celebrity Look-alike Finder")
st.markdown("Upload a photo or take one directly. We'll find which Indian celebrity you resemble most!")

upload_option = st.radio("Choose image source:", ["Upload an image", "Take a photo"])

if upload_option == "Upload an image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
else:
    uploaded_file = st.camera_input("Take a photo")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing..."):
        app = load_insightface_app()
        user_embedding = get_face_embedding(image, app)

        if user_embedding is not None:
            df = load_celeb_data()
            match, similarity = find_best_match(user_embedding, df)

            st.success("✅ Match Found!")
            st.markdown(f"### 🧍 You look like: **{match['celeb_name']}**")
            st.markdown(f"**Similarity:** {similarity * 100:.2f}%")

            if 'desc' in match and pd.notna(match['desc']):
                if st.button("Tell me more about them"):
                    st.markdown(f"📖 {match['desc']}")
                    if 'wikipedia_link' in match and pd.notna(match['wikipedia_link']):
                        st.markdown(f"[🔗 Wikipedia]({match['wikipedia_link']})")
        else:
            st.warning("⚠️ Could not process the image. Make sure it's clear and contains only one face.")
