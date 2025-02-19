import subprocess
import random
import string
from Constants import *

def capture_image(timeout=2000):
    """
    Captures an image using libcamera-still and saves it to the specified path.

    :param timeout: Time (in ms) to allow auto-exposure adjustments before capturing.
    """
    imagePath = constants.imageFolder + random.choices(string.ascii_letters, k = constants.fileNameLength) + ".jpg"
    print(f"📷 Capturing image... Saving to: {imagePath}")
    try:
        subprocess.run(["libcamera-still", "-o", imagePath, "--timeout", str(timeout)], check=True)
        print(f"Image successfully saved: {imagePath}")
    except subprocess.CalledProcessError as e:
        print(f"Capture Image Error: {e}")

# Example usage:
capture_image()
