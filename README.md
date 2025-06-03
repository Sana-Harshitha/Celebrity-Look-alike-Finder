#Celebrity face look a like 🎭

A deep learning-based face recognition project to identify **Indian celebrities** from user-uploaded images. It uses **InsightFace** for 512-dimensional face embeddings, filters images with single faces, and scrapes Wikipedia for descriptions — all packaged in a clean Streamlit web app.

---

## 🚀 Features

- ✅ Scrapes 102 Indian celebrity images from Google
- ✅ Filters valid images with only one face using `face_recognition`
- ✅ Extracts 512-D facial embeddings using **InsightFace**
- ✅ Computes **mean embedding per celebrity**
- ✅ Scrapes descriptions using `WikipediaAPI`
- ✅ Deployable web app via **Streamlit**

---

---

## 🔄 Workflow Overview

### 1. 🖼️ Scrape Celebrity Images
Used `GoogleImageCrawler` from `icrawler` to download 102 Indian celebrity images. Each celebrity’s folder is named like `CI0001`, `CI0002`, ..., and each image `CI0001_001.jpg`, etc.

### 2. 🧼 Filter Valid Images
Used `face_recognition` to retain only images with **exactly one face** for high-quality embedding extraction.

### 3. 🧠 Embedding Extraction (512-D)
Used `InsightFace` to extract embeddings from filtered images:

```python
from insightface.app import FaceAnalysis
Each celeb's embeddings were stored in a dictionary:

python
Copy
Edit
{ 'celeb_name': [embedding1, embedding2, ...] }
And saved using pickle.

4. ➕ Compute Mean Embeddings
Averaged all embeddings per celeb and saved them to:

python
Copy
Edit
data/celeb_mean_embeddings.pkl
5. 📝 Scrape Wikipedia Descriptions
Scraped Wikipedia summaries for each celebrity using:

python
Copy
Edit
import wikipediaapi
wiki = wikipediaapi.Wikipedia('en', user_agent='CelebrityFaceRecognitionBot/1.0')
Saved in:

metadata/celeb_info_scraped.csv (columns: celeb_name, desc)

Merged with embeddings in load_data.py

6. 🌐 Deploy with Streamlit
A user can upload an image, and the app:

Detects the face

Extracts embedding using InsightFace

Compares with mean embeddings using cosine similarity

Displays the most similar celebrity with description

🧪 How to Run
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/celebrity-face-recognition.git
cd celebrity-face-recognition
2. Create virtual environment (optional)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Streamlit app
bash
Copy
Edit
streamlit run app.py
📦 requirements.txt
txt
Copy
Edit
streamlit>=1.30
numpy>=1.24
pandas>=2.0
face_recognition>=1.3.0
opencv-python>=4.8.0
insightface>=0.7.3
wikipedia-api>=0.5.8
scikit-learn>=1.3.0
Pillow>=10.0.0
📸 How Matching Works
Upload image

Detect and crop face

Extract 512-D embedding

Compare with mean embeddings of 102 celebs

Show most similar match with score + description

📈 Example Use Case
Upload an image of Shah Rukh Khan → App detects the face → Compares with mean embeddings → Finds best match and shows Wikipedia description.

🎯 Future Ideas
Support multiple faces per image

Add image confidence score or Top-5 matches

Improve filtering pipeline

Add social media or IMDb links

👩‍💻 Author
Harshitha Sana
📧 harshithasana@google.com

🛡️ License
This project is licensed under the MIT License.

❤️ Acknowledgments
InsightFace

Face Recognition

Wikipedia API

Streamlit

yaml
Copy
Edit

---











