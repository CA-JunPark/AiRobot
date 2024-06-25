import cv2

# Open a connection to the camera
# For Raspberry Pi camera module
cap = cv2.VideoCapture(0)

# For a USB webcam, you might need to specify the device index (usually 0 or 1)
# cap = cv2.VideoCapture(1)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()
else:
    print("Camara detected")

# Capture video until 'q' is pressed
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # If the frame was not captured correctly, break the loop
    if not ret:
        break

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Press 'q' to exit the video capture loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
