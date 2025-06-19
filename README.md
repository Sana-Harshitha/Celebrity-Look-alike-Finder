#  Celebrity Look a Like Finder 

A deep learning-based face recognition system to identify Indian celebrities from user-uploaded images. It uses **InsightFace** for 512-D embeddings, filters images with a single face, scrapes Wikipedia for descriptions, and provides a fast, Streamlit-powered UI.

---

## Features

-  Scrape 102 **INDIAN** celebrity images using `icrawler`(total 3060 images scraped)
-  Filter valid images using `face_recognition`
-  Extract 512-D embeddings via **InsightFace**
-  Compute **mean embeddings** per celebrity
-  Scrape celebrity info using `WikipediaAPI`
-  Deploy with **Streamlit**

---

##  How It Works

### 1. Image Scraping
Used `GoogleImageCrawler` from `icrawler` to scrape 102 Indian celebrity images:
```python
from icrawler.builtin import GoogleImageCrawler
```

### 2. Image Filtering
Used `face_recognition` to retain only images with exactly one face:
```python
import face_recognition
```

### 3. Image Naming Convention
Saved as: `CIXXXXYYY.jpg`  
- `X` = celebrity number (001–102)  
- `Y` = image number for that celebrity

### 4. Embedding Extraction
Used `InsightFace` to extract 512-dimensional embeddings:
```python
from insightface.app import FaceAnalysis
```
Stored as:  
```python
{ 'celeb_name': [embedding1, embedding2, ...] }
```
Saved with:
```python
import pickle

with open("embeddings_insightface.pkl", "wb") as f:
    pickle.dump(embeddings, f)
```

### 5. Mean Embeddings
Averaged all embeddings per celebrity to get one 512-D vector each:
```python
with open(output_path, "wb") as f:
    pickle.dump(mean_embeddings, f)
```

### 6. Metadata CSVs
- `metadata/celeb_mean_embeddings.csv`: celeb_name + 512-D vector  
- `metadata/celeb_info_scraped.csv`: celeb_name, description, wikipedia_link

### 7. Wikipedia Scraping
```python
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='CelebrityFaceRecognitionBot/1.0 (contact: harshithasana@google.com)'
)
```

### 8. Merging Metadata
In `load_data.py`, loaded and merged both CSVs:
- Returns single DataFrame with `embedding`, `desc`, and `wikipedia_link`

### 9. Streamlit App (`app.py`)
- Accepts uploaded user image
- Extracts face embedding
- Computes cosine similarity with database
- Displays best matching celebrity, similarity, and Wikipedia bio

---

## Project Structure

```
celebrity-face-recognition/
├── app.py
├── load_data.py
├── data/
│   ├── filtered_images/
│   ├── embeddings_insightface.pkl
│   └── celeb_mean_embeddings.pkl
├── metadata/
│   ├── celeb_mean_embeddings.csv
│   └── celeb_info_scraped.csv
├── scripts/
│   ├── scrape_images.py
│   ├── filter_images.py
│   ├── generate_embeddings.py
│   ├── generate_mean_embeddings.py
│   ├── data_csv_generater.py
│   └── desc_generater_csv.py
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/celebrity-face-recognition.git
cd celebrity-face-recognition
```

### 2. Create and Activate Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

##  Run the App

```bash
streamlit run app.py
```

---

##  requirements.txt

```txt
streamlit>=1.30
numpy>=1.24
pandas>=2.0
face_recognition>=1.3.0
opencv-python>=4.8.0
insightface>=0.7.3
wikipedia-api>=0.5.8
scikit-learn>=1.3.0
Pillow>=10.0.0
```


---

## Example Flow

1. User uploads a face image
2. Model extracts 512-D vector using InsightFace
3. Cosine similarity is calculated with database
4. Best match is shown with name, similarity score, and description

---

## Future Improvements

- UI improvements
- Add social/influencer links
- Use FAISS for faster vector search

---

##  Author

**Harshitha Sana**  
sanaharshitha2@gmail.com

---

##  Acknowledgments

- [InsightFace](https://github.com/deepinsight/insightface)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [Wikipedia API](https://pypi.org/project/Wikipedia-API/)
- [Streamlit](https://streamlit.io)
- [iCrawler](https://github.com/hellock/icrawler)
