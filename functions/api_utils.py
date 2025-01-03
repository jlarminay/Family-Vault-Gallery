import os
import json
import random
import requests
from config import IMAGES_DIR, IMAGES_JSON_PATH, MAX_IMAGES, API_URL, API_KEY

def fetch_images():
    """Fetch images from API and save to JSON file"""
    try:
      # Fetch images from API
      response = requests.get(API_URL, headers={
        'x-api-token': API_KEY
      })
      response.raise_for_status()
      images = response.json()['images']
      
      if not os.path.isfile(IMAGES_JSON_PATH):
          with open(IMAGES_JSON_PATH, 'w') as f:
              json.dump(images, f, indent=4)
      
      # Shuffle images and save updated list
      random.shuffle(images)
      with open(IMAGES_JSON_PATH, 'w') as f:
          json.dump(images, f, indent=4)
    
    except Exception as e:
      print(f"Error fetching images, using existing images.")

def get_images():
    """Load images from JSON file"""
    with open(IMAGES_JSON_PATH, 'r') as f:
        return json.load(f)

def check_and_download_image(image_url):
    """Check if the image exists; if not, download it"""
    from pathlib import Path
    import requests
    import os

    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)

    image_path = Path(IMAGES_DIR) / Path(image_url).name
    if not image_path.exists():
        # Delete oldest image if the directory exceeds the limit
        if len(os.listdir(IMAGES_DIR)) >= MAX_IMAGES:
            oldest_file = min(Path(IMAGES_DIR).glob('*'), key=os.path.getctime)
            os.remove(oldest_file)
        
        # Download the image
        response = requests.get(image_url)
        response.raise_for_status()
        with open(image_path, 'wb') as f:
            f.write(response.content)
    return image_path