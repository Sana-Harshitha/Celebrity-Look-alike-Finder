import os
import pickle
import numpy as np
import cv2
from insightface.app import FaceAnalysis

def extract_embeddings_insightface(input_root):
    """
    Uses InsightFace to extract face embeddings.
    Returns a dictionary: { 'celeb_name': [embedding1, embedding2, ...] }
    """
    app = FaceAnalysis(name="buffalo_l", providers=['CPUExecutionProvider'])
    app.prepare(ctx_id=0)

    celeb_embeddings = {}

    if not os.path.exists(input_root):
        print(f"Input folder '{input_root}' does not exist.")
        return celeb_embeddings

    celebs = [d for d in os.listdir(input_root) if os.path.isdir(os.path.join(input_root, d))]
    print(f"Found {len(celebs)} celebrity folders in '{input_root}'\n")

    for celeb in celebs:
        print(f" Processing: {celeb}")
        celeb_folder = os.path.join(input_root, celeb)
        image_files = [f for f in os.listdir(celeb_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        embeddings = []
        for img_file in image_files:
            img_path = os.path.join(celeb_folder, img_file)
            try:
                img = cv2.imread(img_path)
                if img is None:
                    print(f" Unable to read {img_path}, skipping.")
                    continue

                faces = app.get(img)
                # if len(faces) == 1:
                #     embeddings.append(faces[0].embedding)
                # else:
                #     print(f"Skipping {img_path} (faces found: {len(faces)})")
                if len(faces) >= 1:
                     # Pick the largest face (by bounding box area)
                    largest_face = max(faces, key=lambda f: f.bbox[2] * f.bbox[3])
                    embeddings.append(largest_face.embedding)
                else:
                    print(f"Skipping {img_path} (no face found)")

            except Exception as e:
                print(f"Error processing {img_path}: {e}")

        celeb_embeddings[celeb] = embeddings
        print(f"Extracted {len(embeddings)} embeddings for {celeb}\n")

    return celeb_embeddings


if __name__ == "__main__":
    input_root = "../data/filtered_images"
    embeddings = extract_embeddings_insightface(input_root)

    # Save embeddings
    save_path = "../data/embeddings_insightface.pkl"
    with open(save_path, "wb") as f:
        pickle.dump(embeddings, f)

    print(f"InsightFace embedding extraction complete. Saved to: {save_path}")
