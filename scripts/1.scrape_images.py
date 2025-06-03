from icrawler.builtin import GoogleImageCrawler
from celeb_list import celebs
import os

def download_images(celebs, max_num=40):
    for celeb in celebs:
        folder = f'../data/images/{celeb.replace(" ", "_")}'
        os.makedirs(folder, exist_ok=True)
        print(f"Downloading for: {celeb}")
        crawler = GoogleImageCrawler(storage={'root_dir': folder})
        crawler.crawl(keyword=celeb, max_num=max_num, min_size=(200, 200))

if __name__ == '__main__':
    download_images(celebs, max_num=30)  
    
