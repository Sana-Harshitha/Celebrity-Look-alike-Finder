import pickle
import csv
import os

# === Load mean embeddings ===
embedding_path = "../data/celeb_mean_embeddings.pkl"  

with open(embedding_path, 'rb') as f:
    mean_embeddings = pickle.load(f)  # {'Shah Rukh Khan': np.array([...]), ...}

# === Create and write CSV ===
output_csv_path = "../metadata/celebs_mean_embeddings.csv"
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header
    header = ['celeb_id', 'celeb_name'] + [f'embedding_{i+1}' for i in range(512)]
    writer.writerow(header)

    # Sort names alphabetically and assign celeb_id
    for idx, celeb_name in enumerate(sorted(mean_embeddings.keys()), start=1):
        celeb_id = f"CI{idx:04d}"  # e.g., CI0001, CI0002, ...
        embedding = mean_embeddings[celeb_name]
        row = [celeb_id, celeb_name] + embedding.tolist()
        writer.writerow(row)

print(f"✅ CSV saved to: {output_csv_path}")
