from time import sleep
while True:
    # absolute path in the Docker Container
    with open ("/home/ros/AiRobot/yolov8/yoloData.txt", mode='r+') as f:
        print(f"read: {f.read()}")