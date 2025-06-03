import face_recognition
import os
from PIL import Image

def filter_single_face_images_for_celeb(input_root, output_root):
    """
    Filters images for each celebrity in input_root folder.
    Keeps only images with exactly one face.
    Saves them in corresponding output_root folder.
    """
    if not os.path.exists(input_root):
        print(f"Input root folder '{input_root}' does not exist.")
        return
    
    os.makedirs(output_root, exist_ok=True)
    
    celebs = [d for d in os.listdir(input_root) if os.path.isdir(os.path.join(input_root, d))]
    
    print(f"Found {len(celebs)} celebrities in {input_root}")
    
    for celeb in celebs:
        input_folder = os.path.join(input_root, celeb)
        output_folder = os.path.join(output_root, celeb)
        os.makedirs(output_folder, exist_ok=True)
        
        print(f"Processing celebrity: {celeb}")
        
        images = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        total_images = len(images)
        saved_count = 0
        
        for img_file in images:
            img_path = os.path.join(input_folder, img_file)
            try:
                image = face_recognition.load_image_file(img_path)
                face_locations = face_recognition.face_locations(image)
                
                if len(face_locations) == 1:
                    # Save image to output folder
                    image_pil = Image.fromarray(image)
                    image_pil.save(os.path.join(output_folder, img_file))
                    saved_count += 1
                
            except Exception as e:
                print(f"Error processing {img_path}: {e}")
        
        print(f"Saved {saved_count}/{total_images} images with exactly one face for {celeb}\n")


if __name__ == "__main__":
    input_root_folder = "../data/images"             
    output_root_folder = "../data/filtered_images"   
    
    filter_single_face_images_for_celeb(input_root_folder, output_root_folder)
