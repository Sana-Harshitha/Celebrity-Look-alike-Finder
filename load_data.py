import pandas as pd
import numpy as np

def load_data(csv_path="./metadata/celebs_mean_embeddings.csv"):
    """
    Loads the celebrity embeddings and metadata from a CSV file.
    Returns:
        A DataFrame with an added 'embedding' column containing 128-D NumPy arrays,
        merged with 'desc' from metadata.
    """
    # Load the embeddings CSV
    df = pd.read_csv(csv_path)

    # Strip whitespace from celeb_name to avoid merge issues
    df['celeb_name'] = df['celeb_name'].astype(str).str.strip()

    # Find all embedding columns
    embedding_cols = [col for col in df.columns if col.startswith("embedding_")]

    # Combine into a single NumPy array per row
    df['embedding'] = df[embedding_cols].values.tolist()
    df['embedding'] = df['embedding'].apply(lambda row: np.array(row, dtype=np.float32))

    # Drop original embedding columns
    df.drop(columns=embedding_cols, inplace=True)

    # Load and clean the metadata
    info_df = pd.read_csv("./metadata/celeb_info_scraped.csv")
    info_df['celeb_name'] = info_df['celeb_name'].astype(str).str.strip()

    # Merge on 'celeb_name'
    merged_df = df.merge(info_df, on="celeb_name", how="left")

    # Fill missing values if any
    merged_df["desc"] = merged_df["desc"].fillna("")
    
    return merged_df

print(load_data())