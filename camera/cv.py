import cv2

# open camera
cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)

# set dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

# take frame
ret, frame = cap.read()
# write frame to file
cv2.imwrite('image.jpg', frame)
# release camera
cap.release()