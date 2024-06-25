# Linyun Liu (2024)
import cv2
from picamera2 import Picamera2
from ultralytics import YOLO

# Initialize the Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280, 720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# Load the YOLOv8 model
model_custom = YOLO("v3.pt")
model_default = YOLO("yolov8n.pt")

def extract(results):
    boxes = results.boxes.xywh.cpu()
    classes = results.boxes.cls.cpu().tolist() # return detected objects ID -> List of int
    names = results.names # return all possible names for dtection -> Dictionary (int: name)
    confs = results.boxes.conf.float().cpu().tolist() # return detected objects confidence score -> List of Float
    output = []
    for i in range(len(classes)):
        result = []
        result.append(names[classes[i]])
        result.append(confs[i])
        output.append(result)    
    
    return output # 2D array, i.e. [[person: 0.92], [cat, 0.67]], [detcted object, confidence score]

import os
try:  
    while True:
        frame = picam2.capture_array()

        # results_c = model_custom(frame)
        results_d = model_default(frame)
        os.system("clear")
        annotated_frame = results_d[0].plot()
        try:
            # result_c = extract(results_c[0])
            result_d = extract(results_d[0])
            # for r in result_c:
            #     print(f"{r[0]}: {r[1]}")
            for r in result_d:
                print(f"{r[0]}: {r[1]}")
        except:
            pass
        cv2.imshow("Camera", annotated_frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()
except KeyboardInterrupt:
    os.system("clear")