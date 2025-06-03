import wikipediaapi
import csv
import time
import os

from celeb_list import celebs  

# Creating Wikipedia object with a valid User-Agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='CelebrityFaceRecognitionBot/1.0 (contact: harshithasana@google.com)'
)

celeb_info = {}

for celeb in celebs:
    page = wiki_wiki.page(celeb)
    
    if page.exists():
        summary = page.summary.split('\n')[0][:400]  
        celeb_info[celeb] = {"desc": summary}
        print(f"✅ {celeb}: {summary[:60]}...")
    else:
        celeb_info[celeb] = {"desc": ""}
        print(f"❌ Page not found for {celeb}")
    
    time.sleep(0.5)  


os.makedirs("../metadata", exist_ok=True)

# Save to CSV
with open("../metadata/celeb_info_scraped.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["celeb_name", "desc"])
    for celeb, info in celeb_info.items():
        writer.writerow([celeb, info["desc"]])

print("✅ Descriptions saved to data/metadata/celeb_info_scraped.csv")
