import pyautogui as pya
import imgs  # Custom module for image searching and clicking
import logging
import time as t

# Constants for image file paths
IMAGE_PATH = "assets/scout.png"  # Replace with your image file path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def search_and_click_scout(image_path, precision=0.8, delay_after_click=125, max_attempts=99):
    """Continuously search for an image on the screen and click it if found."""
    attempt = 0
    while attempt < max_attempts:
        try:
            # Take a screenshot of the current screen
            screenshot = pya.screenshot()
            
            # Search for the image
            position = imgs.imagesearch(image_path, screenshot=screenshot, precision=precision)
            
            if position[0] != -1:
                t.sleep(5)
                # Click on the found image
                imgs.clicking_image(image_path)
                logging.info(f"Clicked on image at position {position}.")
                t.sleep(delay_after_click)  # Wait after clicking
            else:
                logging.warning(f"{image_path} not found on the screen.")
                break
                # t.sleep(5)  # Wait before retrying

            attempt += 1
            
        except Exception as e:
            logging.error(f"Error in search_and_click_scout: {e}")
            return  # Exit on error

    logging.warning("Max attempts reached. Image not found, unable to click, or low happiness.")

if __name__ == "__main__":
    search_and_click_scout(IMAGE_PATH)
