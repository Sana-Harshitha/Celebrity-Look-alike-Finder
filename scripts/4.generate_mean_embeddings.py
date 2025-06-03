import pickle
import numpy as np
import os

def compute_mean_embeddings(raw_embedding_path, output_path):
    """
    Computes the mean embedding for each celebrity.
    Saves the result as a dictionary: { 'celeb_name': mean_embedding }
    """
    if not os.path.exists(raw_embedding_path):
        print(f"Raw embeddings file '{raw_embedding_path}' not found.")
        return

    with open(raw_embedding_path, 'rb') as f:
        raw_embeddings = pickle.load(f)

    mean_embeddings = {}

    for celeb, vectors in raw_embeddings.items():
        if len(vectors) > 0:
            mean_embedding = np.mean(vectors, axis=0)
            mean_embeddings[celeb] = mean_embedding
        else:
            print(f"⚠️ No embeddings found for {celeb}, skipping.")

    with open(output_path, 'wb') as f:
        pickle.dump(mean_embeddings, f)

    print(f"✅ Saved mean embeddings for {len(mean_embeddings)} celebrities to '{output_path}'")


if __name__ == "__main__":
    raw_path = "../data/embeddings_insightface.pkl"   
    output_path = "../data/celeb_mean_embeddings.pkl" 
    compute_mean_embeddings(raw_path, output_path)
