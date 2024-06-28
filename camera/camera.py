from picamera2 import Picamera2
from time import sleep

def main():
    camera = Picamera2()
    camera.start()
    sleep(2)  # Give the camera some time to adjust
    camera.capture_file("/tmp/test_image.jpg")
    camera.stop()
    print("Photo saved as /tmp/test_image.jpg")

if __name__ == "__main__":
    main()
