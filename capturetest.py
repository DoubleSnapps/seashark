from picamera2 import Picamera2
import time

# Initialize the camera
picam2 = Picamera2()

# Configure camera settings
config = picam2.create_still_configuration()
picam2.configure(config)

# Start the camera
picam2.start()
time.sleep(2)  # Allow time for auto-exposure adjustments

# Define image file path
image_path = "/home/pi/captured_image.jpg"

# Capture and save the image
picam2.capture_file(image_path)

print(f"Image saved: {image_path}")
