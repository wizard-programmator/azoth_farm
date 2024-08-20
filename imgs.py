import cv2
import numpy as np
import pyautogui
import time

def imagesearch(image, precision=0.8, screenshot=None):
    """Search for an image in a screenshot and return the position if found."""
    if screenshot is None:
        screenshot = pyautogui.screenshot()

    img_rgb = np.array(screenshot)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val >= precision:
        return max_loc
    return (-1, -1)

def clicking_image(image, precision=0.8, durationL=0.45, durationH=0.75, offset=0, amount_of_clicks=1, time_between_clicks=1):
    """Search for an image and click on it if found."""
    pos = imagesearch(image, precision)
    
    if pos[0] != -1:
        offsetX = np.random.uniform(-offset, offset)
        offsetY = np.random.uniform(-offset, offset)

        pyautogui.moveTo(pos[0] + offsetX, pos[1] + offsetY, duration=np.random.uniform(durationL, durationH))
        time.sleep(np.random.uniform(0, 0.15))
        
        for _ in range(amount_of_clicks):
            pyautogui.click(pos[0] + offsetX, pos[1] + offsetY)
            print(f"Clicked on {image} at position {pos[0] + offsetX}, {pos[1] + offsetY}")
            time.sleep(time_between_clicks)
    else:
        print(f"{image} not found!")

if __name__ == "__main__":
    # Example usage
    image_path = "assets/example_image.png"  # Replace with the path to your image file
    clicking_image(image_path)
