import pyautogui as pya
import imgs  # Custom module for image searching and clicking
import logging
import time as t

# Constants for image file paths based on resolution
IMAGE_PATHS = {
    "1920x1080": "assets/1920x1080/scout.png",
    "1760x990": "assets/1760x990/scout.png",
    "1680x1050": "assets/1680x1050/scout.png",
    "1600x900": "assets/1600x900/scout.png",
    "1366x768": "assets/1366x768/scout.png",
    "1280x1024": "assets/1280x1024/scout.png",
    "1280x720": "assets/1280x720/scout.png",
    "1128x634": "assets/1128x634/scout.png",
    "1024x768": "assets/1024x768/scout.png",
    "800x600": "assets/800x600/scout.png"
}

# Predefined resolutions
RESOLUTIONS = {
    "1920x1080": (1920, 1080),
    "1760x990": (1760, 990),
    "1680x1050": (1680, 1050),
    "1600x900": (1600, 900),
    "1366x768": (1366, 768),
    "1280x1024": (1280, 1024),
    "1280x720": (1280, 720),
    "1128x634": (1128, 634),
    "1024x768": (1024, 768),
    "800x600": (800, 600)
}

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def prompt_for_resolution():
    """Prompt the user to select a resolution from the predefined list."""
    print("Select a resolution from the following options:")
    for index, (resolution, dimensions) in enumerate(RESOLUTIONS.items(), 1):
        print(f"{index}. {resolution} ({dimensions[0]}x{dimensions[1]})")
    
    while True:
        try:
            choice = int(input("Enter the number corresponding to your resolution choice: "))
            if 1 <= choice <= len(RESOLUTIONS):
                resolution_key = list(RESOLUTIONS.keys())[choice - 1]
                print(f"You selected: {resolution_key}")
                return resolution_key
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def search_and_click_scout(image_path, precision=0.8, delay_after_click=125, max_attempts=99):
    """Continuously search for an image on the screen and click it if found."""
    attempt = 0
    while attempt < max_attempts:
        try:
            t.sleep(5)  # Delay before each attempt
            # Take a screenshot of the current screen
            screenshot = pya.screenshot()
            screenshot.save("screenshot.png")  # Save screenshot for debugging
            logging.info("Screenshot saved as screenshot.png")

            # Search for the image within the screenshot
            position = imgs.imagesearch(image_path, screenshot=screenshot, precision=precision)
            logging.info(f"Image search result: {position}")

            if position[0] != -1:
                logging.info(f"Image found at position {position}.")
                t.sleep(5)  # Short delay before clicking
                # Click on the found image
                imgs.clicking_image(image_path)
                logging.info(f"Clicked on image at position {position}.")
                t.sleep(delay_after_click)  # Wait after clicking
            else:
                logging.warning(f"{image_path} not found on the screen.")
                attempt += 1
                continue

            break
            
        except Exception as e:
            logging.error(f"Error in search_and_click_scout: {e}")
            return

    logging.warning("Max attempts reached. Image not found, unable to click, or low happiness.")

if __name__ == "__main__":
    resolution_key = prompt_for_resolution()
    if resolution_key:
        image_path = IMAGE_PATHS.get(resolution_key)
        if image_path:
            search_and_click_scout(image_path)
        else:
            logging.error("No image path available for the selected resolution.")
