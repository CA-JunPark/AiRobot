from picamera2 import Picamera2
import time

# Create a Picamera2 object
picam2 = Picamera2()

# Configure the camera
camera_config = picam2.create_still_configuration()

# Apply the configuration to the camera
picam2.configure(camera_config)

# Start the camera
picam2.start()

# Wait for the camera to adjust
time.sleep(2)

# Capture an image and save it to a file
picam2.capture_file("test_image.jpg")

# Stop the camera
picam2.stop()

