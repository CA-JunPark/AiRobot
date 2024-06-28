import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video device")
else:
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("/tmp/test_image.jpg", frame)
        print("Photo saved as /tmp/test_image.jpg")
    else:
        print("Failed to capture image")

    cap.release()
