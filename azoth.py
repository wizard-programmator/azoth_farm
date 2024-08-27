import pyautogui as pya
import imgs  # Custom module for image searching and clicking
import logging
import os
import time as t
from pynput.keyboard import Key, Controller
import random


# Constants for image file paths based on resolution
IMAGE_PATHS = {
    "1920x1080": {
        "scout1": "assets/1920x1080/scout1.png",
        "scout2": "assets/1920x1080/scout2.png",
        "pet": "assets/1920x1080/pet.png",
        "snack": "assets/1920x1080/snack.png",
        "food": "assets/1920x1080/food.png",
        "feed": "assets/1920x1080/feed.png",
        "wizard101": "assets/1920x1080/wizard101.png",
        "close": "assets/1920x1080/close.png",
        "book": "assets/1920x1080/book.png",
        "option": "assets/1920x1080/option.png",
        "realms": "assets/1920x1080/realms.png",
        "next_realm": "assets/1920x1080/next_realm.png",
        "realm_name": "assets/1920x1080/realm_name.png",
        "go_to_realm": "assets/1920x1080/go_to_realm.png"
    },
    "1760x990": {
        "scout": "assets/1760x990/scout.png",
        "pet": "assets/1760x990/pet.png",
        "snack": "assets/1760x990/snack.png",
        "food": "assets/1760x990/food.png",
        "feed": "assets/1760x990/feed.png",
        "wizard101": "assets/1760x990/wizard101.png",
        "close": "assets/1760x990/close.png",
        "book": "assets/1760x990/book.png",
        "option": "assets/1760x990/option.png",
        "realms": "assets/1760x990/realms.png",
        "next_realm": "assets/1760x990/next_realm.png",
        "realm_name": "assets/1760x990/realm_name.png",
        "go_to_realm": "assets/1760x990/go_to_realm.png"
    },
    "1680x1050": {
        "scout": "assets/1680x1050/scout.png",
        "pet": "assets/1680x1050/pet.png",
        "snack": "assets/1680x1050/snack.png",
        "food": "assets/1680x1050/food.png",
        "feed": "assets/1680x1050/feed.png",
        "wizard101": "assets/1680x1050/wizard101.png",
        "close": "assets/1680x1050/close.png",
        "book": "assets/1680x1050/book.png",
        "option": "assets/1680x1050/option.png",
        "realms": "assets/1680x1050/realms.png",
        "next_realm": "assets/1680x1050/next_realm.png",
        "realm_name": "assets/1680x1050/realm_name.png",
        "go_to_realm": "assets/1680x1050/go_to_realm.png"
    },
    "1600x900": {
        "scout": "assets/1600x900/scout.png",
        "pet": "assets/1600x900/pet.png",
        "snack": "assets/1600x900/snack.png",
        "food": "assets/1600x900/food.png",
        "feed": "assets/1600x900/feed.png",
        "wizard101": "assets/1600x900/wizard101.png",
        "close": "assets/1600x900/close.png",
        "book": "assets/1600x900/book.png",
        "option": "assets/1600x900/option.png",
        "realms": "assets/1600x900/realms.png",
        "next_realm": "assets/1600x900/next_realm.png",
        "realm_name": "assets/1600x900/realm_name.png",
        "go_to_realm": "assets/1600x900/go_to_realm.png"
    },
    "1366x768": {
        "scout": "assets/1366x768/scout.png",
        "pet": "assets/1366x768/pet.png",
        "snack": "assets/1366x768/snack.png",
        "food": "assets/1366x768/food.png",
        "feed": "assets/1366x768/feed.png",
        "wizard101": "assets/1366x768/wizard101.png",
        "close": "assets/1366x768/close.png",
        "book": "assets/1366x768/book.png",
        "option": "assets/1366x768/option.png",
        "realms": "assets/1366x768/realms.png",
        "next_realm": "assets/1366x768/next_realm.png",
        "realm_name": "assets/1366x768/realm_name.png",
        "go_to_realm": "assets/1366x768/go_to_realm.png"
    },
    "1280x1024": {
        "scout": "assets/1280x1024/scout.png",
        "pet": "assets/1280x1024/pet.png",
        "snack": "assets/1280x1024/snack.png",
        "food": "assets/1280x1024/food.png",
        "feed": "assets/1280x1024/feed.png",
        "wizard101": "assets/1280x1024/wizard101.png",
        "close": "assets/1280x1024/close.png",
        "book": "assets/1280x1024/book.png",
        "option": "assets/1280x1024/option.png",
        "realms": "assets/1280x1024/realms.png",
        "next_realm": "assets/1280x1024/next_realm.png",
        "realm_name": "assets/1280x1024/realm_name.png",
        "go_to_realm": "assets/1280x1024/go_to_realm.png"
    },
    "1280x720": {
        "scout": "assets/1280x720/scout.png",
        "pet": "assets/1280x720/pet.png",
        "snack": "assets/1280x720/snack.png",
        "food": "assets/1280x720/food.png",
        "feed": "assets/1280x720/feed.png",
        "wizard101": "assets/1280x720/wizard101.png",
        "close": "assets/1280x720/close.png",
        "book": "assets/1280x720/book.png",
        "option": "assets/1280x720/option.png",
        "realms": "assets/1280x720/realms.png",
        "next_realm": "assets/1280x720/next_realm.png",
        "realm_name": "assets/1280x720/realm_name.png",
        "go_to_realm": "assets/1280x720/go_to_realm.png"
    },
    "1128x634": {
        "scout": "assets/1128x634/scout.png",
        "pet": "assets/1128x634/pet.png",
        "snack": "assets/1128x634/snack.png",
        "food": "assets/1128x634/food.png",
        "feed": "assets/1128x634/feed.png",
        "wizard101": "assets/1128x634/wizard101.png",
        "close": "assets/1128x634/close.png",
        "book": "assets/1128x634/book.png",
        "option": "assets/1128x634/option.png",
        "realms": "assets/1128x634/realms.png",
        "next_realm": "assets/1128x634/next_realm.png",
        "realm_name": "assets/1128x634/realm_name.png",
        "go_to_realm": "assets/1128x634/go_to_realm.png"
    },
    "1024x768": {
        "scout": "assets/1024x768/scout.png",
        "pet": "assets/1024x768/pet.png",
        "snack": "assets/1024x768/snack.png",
        "food": "assets/1024x768/food.png",
        "feed": "assets/1024x768/feed.png",
        "wizard101": "assets/1024x768/wizard101.png",
        "close": "assets/1024x768/close.png",
        "book": "assets/1024x768/book.png",
        "option": "assets/1024x768/option.png",
        "realms": "assets/1024x768/realms.png",
        "next_realm": "assets/1024x768/next_realm.png",
        "realm_name": "assets/1024x768/realm_name.png",
        "go_to_realm": "assets/1024x768/go_to_realm.png"
    },
    "800x600": {
        "scout1": "assets/800x600/scout1.png",
        "scout2": "assets/800x600/scout2.png",
        "pet": "assets/800x600/pet.png",
        "snack": "assets/800x600/snack.png",
        "food": "assets/800x600/food.png",
        "feed": "assets/800x600/feed.png",
        "wizard101": "assets/800x600/wizard101.png",
        "close": "assets/800x600/close.png",
        "book": "assets/800x600/book.png",
        "option": "assets/800x600/option.png",
        "realms": "assets/800x600/realms.png",
        "next_realm": "assets/800x600/next_realm.png",
        "realm_name": "assets/800x600/realm_name.png",
        "go_to_realm": "assets/800x600/go_to_realm.png"
    }
}


# Predefined screen resolutions
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

# Configure logging to show time, log level, and message
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')








def prompt_for_resolution():
    """
    Prompt the user to select a resolution from the predefined list.
    Returns:
        str: The selected resolution key.
    """
    print("Select a resolution from the following options:")
    for index, resolution in enumerate(IMAGE_PATHS.keys(), 1):
        print(f"{index}. {resolution}")

    while True:
        try:
            choice = int(input("Enter the number corresponding to your resolution choice: "))
            if 1 <= choice <= len(IMAGE_PATHS):
                resolution_key = list(IMAGE_PATHS.keys())[choice - 1]
                print(f"You selected: {resolution_key}")
                return resolution_key
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def file_exists(file_path):
    """
    Check if a file exists.
    Args:
        file_path (str): Path to the file.
    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def search_image(image_path, precision=0.8):
    """
    Search for an image on the screen and return its position.
    Args:
        image_path (str): Path to the image file.
        precision (float): Precision of the image search.
    Returns:
        tuple or None: Position of the image if found, otherwise None.
    """
    try:
        screenshot = pya.screenshot()
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)
        logging.debug("Screenshot saved as screenshot.png")

        position = imgs.imagesearch(image_path, screenshot=screenshot, precision=precision)
        logging.debug(f"Image search result: {position}")

        if position and position[0] != -1:
            logging.info(f"Image found at position {position}.")
            return position
        else:
            logging.warning(f"Image {image_path} not found.")
            return None

    except Exception as e:
        logging.error(f"Error in search_image: {e}")
        return None

def click_image(image_path, precision=0.8):
    """
    Search for an image on the screen and click it if found.
    Args:
        image_path (str): Path to the image file.
        precision (float): Precision of the image search.
    Returns:
        bool: True if the image was found and clicked, False otherwise.
    """
    if not file_exists(image_path):
        logging.error(f"Image path {image_path} is missing or file does not exist.")
        return False

    try:
        position = search_image(image_path, precision)
        if position:
            imgs.clicking_image(image_path)
            logging.info(f"Clicked on image {image_path} at position {position}.")
            return True
        return False
    except Exception as e:
        logging.error(f"Error in click_image: {e}")
        return False

def change_realm():
    """
    Perform the sequence of clicks to change the realm.
    """
    if click_image('assets/800x600/book.png'):
        t.sleep(1)  # Wait for the menu to open
        
        if click_image("assets/800x600/option.png"):
            t.sleep(1)
            
            if click_image("assets/800x600/realms.png"):
                t.sleep(1)
                
                for _ in range(random.randint(1, 5)):
                    if not click_image("assets/800x600/next_realm.png"):
                        logging.error("Failed to click 'Next'.")
                        return
                
                t.sleep(1)
                
                if click_image("assets/800x600/realm_name.png"):
                    t.sleep(1)
                    
                    if not click_image("assets/800x600/go_to_realm.png"):
                        logging.error("Failed to click 'Go to Realm'.")
    else:
        logging.error("Failed to click the book.")

def perform_sequence(resolution_key):
    """
    Perform a sequence of actions based on the availability of images.
    Args:
        resolution_key (str): The selected screen resolution key.
    """
    image_paths = IMAGE_PATHS.get(resolution_key, {})

    # Function to handle clicking an image and logging its status
    def handle_image(image_key):
        """
        Handle clicking an image and logging its status.
        Args:
            image_key (str): The key for the image in IMAGE_PATHS.
        Returns:
            bool: True if the image was clicked, False otherwise.
        """
        image_path = image_paths.get(image_key)
        return click_image(image_path) if image_path else False

    # First, handle scout1 and scout2
    if handle_image("scout1") or handle_image("scout2"):
        t.sleep(125)  # Wait for 2 minutes before proceeding to the next actions
        return  # Exit after handling scout1 or scout2

    # If scout1 and scout2 are not found, proceed with other actions
    if handle_image("snack"):
        if check_happiness():  # Only click food if happiness is not detected
            handle_image("food")
        handle_image("feed")
        handle_image("close")
        t.sleep(1)  # Wait 1 second before trying Scout
    else:
        handle_image("pet")

    handle_image("close")
    t.sleep(1)  # Wait 1 second before trying Scout

    # Finally, change the realm
    change_realm()



def press_key(d_duration=2):
    """
    Simulate pressing 'D' key with a specified duration.
    Args:
        d_duration (int): Duration to press the 'D' key in seconds.
    """
    keyboard = Controller()
    
    try:
        keyboard.press('d')
        logging.info(f"D key pressed down.")
        t.sleep(d_duration)
        keyboard.release('d')
        logging.info(f"D key released.")
    except Exception as e:
        logging.error(f"Error in press_key: {e}")

def wait_for_image(image_path, precision=0.8, wait_time=60):
    """
    Wait for an image to appear on the screen with a countdown.
    Args:
        image_path (str): Path to the image file.
        precision (float): Precision of the image search.
        wait_time (int): Maximum time to wait for the image in seconds.
    Returns:
        bool: True if the image is found, False if timeout occurs.
    """
    start_time = t.time()
    end_time = start_time + wait_time

    while True:
        if click_image(image_path, precision):
            logging.info(f"Found {image_path}.")
            
            if image_path == IMAGE_PATHS[resolution_key]["wizard101"]:
                press_key()
            return True

        remaining_time = int(end_time - t.time())
        if remaining_time <= 0:
            logging.error(f"Timeout waiting for {image_path}.")
            return False

        print(f"\rTime remaining: {remaining_time} seconds", end="")
        t.sleep(1)

if __name__ == "__main__":
    resolution_key = prompt_for_resolution()

    wizard101_image_path = IMAGE_PATHS[resolution_key]["wizard101"]
    if not wait_for_image(wizard101_image_path, precision=0.8):
        logging.error("The 'wizard101' image was not found within the timeout period. Exiting the script.")
        exit(1)

    t.sleep(5)  # Initial wait before starting the main loop

    while True:
        try:
            perform_sequence(resolution_key)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
        # Uncomment the line below if you want to wait for 2 minutes before the next search
        # t.sleep(120)
