import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
IMAGE_DISPLAY_TIME = int(os.getenv('IMAGE_DISPLAY_TIME', 5))
SCREEN_WIDTH = int(os.getenv('SCREEN_WIDTH', 1024))
SCREEN_HEIGHT = int(os.getenv('SCREEN_HEIGHT', 600))
NEXT_IMAGE_PATH = "next_image.jpg"
TOUCHSCREEN_DEVICE = os.getenv('TOUCHSCREEN_DEVICE', '/dev/input/event0')
IMAGES_DIR = 'images'
IMAGES_JSON_PATH = 'images.json'
MAX_IMAGES = 10  # Adjust this limit based on available memory

# API
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')
