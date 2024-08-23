import pyautogui as pya
import imgs  # Custom module for image searching and clicking
import logging
import os
import time as t


# Constants for image file paths based on resolution
IMAGE_PATHS = {
    "1920x1080": {
        "scout": "assets/1920x1080/scout.png",
        "pet": "assets/1920x1080/pet.png",
        "snack": "assets/1920x1080/snack.png",
        "food": "assets/1920x1080/food.png",
        "feed": "assets/1920x1080/feed.png",
        "wizard101": "assets/1920x1080/wizard101.png",
        "close": "assets/1920x1080/close.png"
    },
    "1760x990": {
        "scout": "assets/1760x990/scout.png",
        "pet": "assets/1760x990/pet.png",
        "snack": "assets/1760x990/snack.png",
        "food": "assets/1760x990/food.png",
        "feed": "assets/1760x990/feed.png",
        "wizard101": "assets/1760x990/wizard101.png",
        "close": "assets/1760x990/close.png"
    },
    "1680x1050": {
        "scout": "assets/1680x1050/scout.png",
        "pet": "assets/1680x1050/pet.png",
        "snack": "assets/1680x1050/snack.png",
        "food": "assets/1680x1050/food.png",
        "feed": "assets/1680x1050/feed.png",
        "wizard101": "assets/1680x1050/wizard101.png",
        "close": "assets/1680x1050/close.png"
    },
    "1600x900": {
        "scout": "assets/1600x900/scout.png",
        "pet": "assets/1600x900/pet.png",
        "snack": "assets/1600x900/snack.png",
        "food": "assets/1600x900/food.png",
        "feed": "assets/1600x900/feed.png",
        "wizard101": "assets/1600x900/wizard101.png",
        "close": "assets/1600x900/close.png"
    },
    "1366x768": {
        "scout": "assets/1366x768/scout.png",
        "pet": "assets/1366x768/pet.png",
        "snack": "assets/1366x768/snack.png",
        "food": "assets/1366x768/food.png",
        "feed": "assets/1366x768/feed.png",
        "wizard101": "assets/1366x768/wizard101.png",
        "close": "assets/1366x768/close.png"
    },
    "1280x1024": {
        "scout": "assets/1280x1024/scout.png",
        "pet": "assets/1280x1024/pet.png",
        "snack": "assets/1280x1024/snack.png",
        "food": "assets/1280x1024/food.png",
        "feed": "assets/1280x1024/feed.png",
        "wizard101": "assets/1280x1024/wizard101.png",
        "close": "assets/1280x1024/close.png"
    },
    "1280x720": {
        "scout": "assets/1280x720/scout.png",
        "pet": "assets/1280x720/pet.png",
        "snack": "assets/1280x720/snack.png",
        "food": "assets/1280x720/food.png",
        "feed": "assets/1280x720/feed.png",
        "wizard101": "assets/1280x720/wizard101.png",
        "close": "assets/1280x720/close.png"
    },
    "1128x634": {
        "scout": "assets/1128x634/scout.png",
        "pet": "assets/1128x634/pet.png",
        "snack": "assets/1128x634/snack.png",
        "food": "assets/1128x634/food.png",
        "feed": "assets/1128x634/feed.png",
        "wizard101": "assets/1128x634/wizard101.png",
        "close": "assets/1128x634/close.png"
    },
    "1024x768": {
        "scout": "assets/1024x768/scout.png",
        "pet": "assets/1024x768/pet.png",
        "snack": "assets/1024x768/snack.png",
        "food": "assets/1024x768/food.png",
        "feed": "assets/1024x768/feed.png",
        "wizard101": "assets/1024x768/wizard101.png",
        "close": "assets/1024x768/close.png"
    },
    "800x600": {
        "scout1": "assets/800x600/scout1.png",
        "scout2": "assets/800x600/scout2.png",
        "pet": "assets/800x600/pet.png",
        "snack": "assets/800x600/snack.png",
        "food": "assets/800x600/food.png",
        "feed": "assets/800x600/feed.png",
        "wizard101": "assets/800x600/wizard101.png",
        "close": "assets/800x600/close.png"
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
        screenshot.save(screenshot_path)  # Save screenshot for debugging
        logging.debug("Screenshot saved as screenshot.png")

        # Use custom image search function from imgs module
        position = imgs.imagesearch(image_path, screenshot=screenshot, precision=precision)
        logging.debug(f"Image search result: {position}")

        if position[0] != -1:
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
    if not image_path or not file_exists(image_path):
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
    


def perform_sequence(resolution_key):
    """
    Perform a sequence of actions based on the availability of images.
    Args:
        resolution_key (str): The selected screen resolution key.
    """    
    image_paths = IMAGE_PATHS.get(resolution_key, {})
    resolution = RESOLUTIONS.get(resolution_key, (0, 0))
    width, height = resolution

    def click_center():
        """Click the center of the screen based on the resolution."""
        center_x = width // 2
        center_y = height // 2
        pya.click(center_x, center_y)
        logging.info(f"Clicked center of the screen at ({center_x}, {center_y})")

    # Step 1: Attempt to click Scout
    if click_image(image_paths.get("scout1")) or click_image(image_paths.get("scout2")):
        click_center()
        t.sleep(125)  # Wait for 2 minutes before the next action
        return
    
    # Step 2: If Scout not found, check for Snack
    if click_image(image_paths.get("snack")):
        if click_image(image_paths.get("food")):
            if click_image(image_paths.get("feed")):
                click_image(image_paths.get("close"))
            else:
                click_image(image_paths.get("close"))
            t.sleep(1)  # Wait 1 second before trying Scout
        else:
            click_image(image_paths.get("close"))
            t.sleep(1)  # Wait 1 second before trying Scout
    else:
        click_image(image_paths.get("pet"))
        return

    click_image(image_paths.get("close"))
    t.sleep(1)  # Wait 1 second before trying Scout




def press_key(d_duration=2):
    """
    Simulate pressing 'D' and 'Ctrl' keys with specified durations.
    
    Args:
        d_duration (int): Duration to press the 'D' key in seconds.
        ctrl_duration (int): Duration to hold down the 'Ctrl' key in seconds.
    """    
    keyboard = Controller()
    
    try:
        # Press and hold 'D' key
        keyboard.press('d')
        logging.info(f"D key pressed down.")
        
        # Wait for the duration while 'D' key is held
        t.sleep(d_duration)
        
        
    except Exception as e:
        logging.error(f"Error in press_d_then_ctrl: {e}")
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

        # Print the countdown
        print(f"\rTime remaining: {remaining_time} seconds", end="")
        t.sleep(1)  # Wait for 1 second before checking again

    # Note: The above code will never reach this point due to the while loop,
    # but it's good practice to return something in case the loop is ever exited.
    return False


if __name__ == "__main__":
    # Prompt user for resolution
    resolution_key = prompt_for_resolution()

    # Wait for the "wizard101" image to appear before running the script
    wizard101_image_path = IMAGE_PATHS[resolution_key]["wizard101"]
    if not wait_for_image(wizard101_image_path, precision=0.8):
        logging.error("The 'wizard101' image was not found within the timeout period. Exiting the script.")
        exit(1)  # Exit the script if 'wizard101' is not found

    t.sleep(5)  # Initial wait before starting the main loop

    while True:
        try:
            perform_sequence(resolution_key)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
        # Uncomment the line below if you want to wait for 2 minutes before the next search
        # t.sleep(120)