import pyautogui as pya
import imgs  # Custom module for image searching and clicking
import logging
import os
import time as t
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
        "go_to_realm": "assets/800x600/go_to_realm.png",
        "center": "assets/800x600/center.png",
        "happiness": "assets/800x600/happiness.png"
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




def file_exists(file_path):
    return os.path.isfile(file_path)


def search_image(image_path, precision=0.8):
    try:
        screenshot = pya.screenshot()
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)
        
        # Search for the image on the screen
        position = imgs.imagesearch(image_path, screenshot=screenshot, precision=precision)
        
        # Clean up the screenshot file after using it
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)  # Delete the screenshot file
        
        # Return the position of the found image
        return position if position and position[0] != -1 else None
    except Exception as e:
        logging.error(f"Error in search_image: {e}")
        return None


def click_image(image_path, precision=0.8):
    if not file_exists(image_path):
        logging.error(f"Image {image_path} is missing or does not exist.")
        return False
    try:
        position = search_image(image_path, precision)
        if position:
            imgs.clicking_image(image_path)
            logging.info(f"Clicked image {image_path}")
            return True
        return False
    except Exception as e:
        logging.error(f"Error in click_image: {e}")
        return False


    
    

def click_center(resolution_key, precision=0.8):
    """
    Search for the center image on the screen and click it.
    
    Args:
        resolution_key (str): The selected screen resolution key.
        precision (float): Precision of the image search.
    Returns:
        bool: True if the image was found and clicked, False otherwise.
    """
    image_paths = IMAGE_PATHS.get(resolution_key, {})
    center_image_path = image_paths.get("wizard101")  # Get the center image path based on resolution
    
    if not file_exists(center_image_path):
        logging.error(f"Center image for resolution {resolution_key} is missing or file does not exist.")
        return False

    try:
        if click_image(center_image_path, precision):  # Directly click the center image if found
            logging.info(f"Clicked the center image: {center_image_path}")
            return True
        else:
            logging.warning(f"Center image {center_image_path} not found.")
            return False
    except Exception as e:
        logging.error(f"Error in click_center: {e}")
        return False


    


def check_happiness(resolution_key, precision=0.8):
    image_paths = IMAGE_PATHS.get(resolution_key, {})
    happiness_image_path = image_paths.get("happiness")
    if not file_exists(happiness_image_path):
        logging.error(f"Happiness image for resolution {resolution_key} is missing or file does not exist.")
        return False

    try:
        if click_image(happiness_image_path, precision):
            logging.info(f"Clicked the happiness image: {happiness_image_path}")
            return True
        else:
            logging.warning(f"Happiness image {happiness_image_path} not found.")
            return False
    except Exception as e:
        logging.error(f"Error in check_happiness: {e}")
        return False
    
    # happiness_image_path = IMAGE_PATHS.get(resolution_key).get('happiness')
    # return happiness_image_path and click_image(happiness_image_path)


def change_realm(resolution_key, max_retries=3):
    """
    Perform the sequence of clicks to change the realm. If "Go to Realm" is unavailable, retry clicking "Next Realm".
    
    Args:
        resolution_key (str): The selected screen resolution key.
        max_retries (int): Number of times to retry if "Go to Realm" is unavailable.
    """
    image_paths = IMAGE_PATHS[resolution_key]
    retry_count = 0

    # Step 1: Open the menu to change realms
    if click_image(image_paths['book']):
        t.sleep(1)  # Wait for the menu to open
        
        if click_image(image_paths['option']):
            t.sleep(1)
            
            if click_image(image_paths['realms']):
                t.sleep(1)
                
                # Step 2: Click "Next Realm" randomly between 1 and 4 times
                for _ in range(random.randint(1, 5)):
                    click_image(image_paths['next_realm'])
                    t.sleep(1)
                
                # Step 3: Try to click "Go to Realm", retry if unavailable
                while retry_count < max_retries:
                    if click_image(image_paths['realm_name']):
                        t.sleep(1)
                        
                        if click_image(image_paths['go_to_realm']):
                            logging.info("Successfully changed realm.")
                            return True  # Exit function if realm change is successful
                        else:
                            logging.warning("Go to Realm unavailable, retrying with Next Realm.")
                            # If "Go to Realm" is unavailable, click "Next Realm" again
                            click_image(image_paths['next_realm'])
                            retry_count += 1
                            t.sleep(1)  # Small delay before retrying
                    else:
                        logging.error("Realm name not found.")
                        return False
    else:
        logging.error("Failed to open the book menu.")
    
    logging.error("Failed to change the realm after retries.")
    return False



def perform_main_sequence(resolution_key):
    image_paths = IMAGE_PATHS[resolution_key]
    
    # Try to click scout1 or scout2 and click center, repeat after 130 seconds
    if click_image(image_paths['scout1']) or click_image(image_paths['scout2']):
        click_center(resolution_key)
        t.sleep(130)
        return True
    
    # If scout is not found, click pet and retry
    if click_image(image_paths['pet']):
        # Retry clicking scout after clicking pet
        if click_image(image_paths.get('scout1')) or click_image(image_paths.get('scout2')):
            logging.info("Found scout after clicking pet, clicking center.")
            click_center(resolution_key)
            t.sleep(130)  # Wait 130 seconds before proceeding
            return True  # Exit the loop
        
        # If scout is still not found, proceed with snack check    
        logging.info("Scout not found after retrying. Checking for snack.")
        # Try to find snack after clicking pet
        if not click_image(image_paths['snack']):
            # If snack is not found, click center, then click pet again
            logging.info("Snack not found, clicking center and retrying pet.")
            click_center(resolution_key)
            t.sleep(1)  # Small delay
            # Click pet again after center click
            if click_image(image_paths['pet']):
                logging.info("Clicked pet again after clicking center.")
                # After retrying pet, try scout again
                if click_image(image_paths['scout1']) or click_image(image_paths['scout2']):
                    click_center(resolution_key)
                    t.sleep(130)
                    return True
    
    # If scout not found after pet, click snack
    if click_image(image_paths['snack']):
        if check_happiness(resolution_key):  # If happiness, click food and feed
            click_image(image_paths['food'])
            click_image(image_paths['feed'])
            click_image(image_paths['close'])
        else:  # If no happiness, close and change realms
            click_image(image_paths['close'])
            change_realm(resolution_key)
            t.sleep(5)
    return False


def perform_sequence(resolution_key):
    while True:
        if perform_main_sequence(resolution_key):
            continue
        else:
            t.sleep(1)  # Short wait before retrying

        
def prompt_for_resolution():
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


if __name__ == "__main__":
    resolution_key = prompt_for_resolution()
    t.sleep(5)
    perform_sequence(resolution_key)