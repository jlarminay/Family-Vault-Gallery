import time
import threading
from config import IMAGE_DISPLAY_TIME, NEXT_IMAGE_PATH, IMAGES_DIR, MAX_IMAGES
from functions.api_utils import fetch_images, get_images, check_and_download_image
from functions.image_utils import resize_and_pad_image, display_image
from functions.touch_utils import open_touchscreen_device, touch_detected

def prepare_next_image(next_image_path):
    resize_and_pad_image(next_image_path, NEXT_IMAGE_PATH)

def main():
    # Fetch and prepare images
    fetch_images()
    images = get_images()

    # Prepare the first image
    current_image_index = 0
    next_image_remote_url = images[current_image_index]['path']
    
    next_image_path = check_and_download_image(next_image_remote_url)
    prepare_next_image(next_image_path)
    
    # Open the touchscreen device
    touchscreen = open_touchscreen_device()

    while True:
        # Display the image
        display_image(NEXT_IMAGE_PATH)

        # Start a thread to prepare the next image while displaying the current one
        current_image_index = (current_image_index + 1) % len(images)
        next_image_path = check_and_download_image(images[current_image_index]['path'])
        preparation_thread = threading.Thread(target=prepare_next_image, args=(next_image_path,))
        preparation_thread.start()

        # # Wait for display time or a touch event
        # start_time = time.time()
        # while time.time() - start_time < IMAGE_DISPLAY_TIME:
        #     if touch_detected(touchscreen):
        #         print("Touch detected! Moving to the next image.")
        #         break
        #     time.sleep(0.1)  # Polling interval

        time.sleep(IMAGE_DISPLAY_TIME)

if __name__ == "__main__":
    main()
