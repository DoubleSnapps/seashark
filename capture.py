import subprocess
import random
import string
from Constants import *

def capture_image(exposure=2000):
    """
    Captures an image using libcamera-still and saves it to the specified path.

    :param timeout: exposure time (in ms) 
    """
    imagePath = constants.imageFolder + ''.join(random.choices(string.ascii_letters, k = constants.fileNameLength)) + ".jpg"
    print(f"📷 Capturing image... Saving to: {imagePath}")
    try:
        subprocess.run(["libcamera-still", "-o", imagePath, "--timeout", str(exposure)], check=True)
        print(f"Image successfully saved: {imagePath}")
    except subprocess.CalledProcessError as e:
        print(f"Capture Image Error: {e}")
