from ultralytics import YOLO
import cv2
import cvzone
import torch

# cap = cv2.VideoCapture(0) #Webcam
# cap.set(3, 1280)
# cap.set(4, 720)
cap=cv2.VideoCapture("../video/10.mp4")  #For Video


model = YOLO("../Yolo_weights/yolov8n.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush","pen"
              ]

while True:
    success, img = cap.read()
    if not success:
        continue


    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes

        for box in boxes:
            #BOUNDING BOX METHOD
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            #CONFIDENCE METHOD

            confidence = (box.conf[0].cpu().numpy())*100  # Convert confidence to numpy
            print(f"Confidence: {confidence:.2f}%")

            # cvzone.putTextRect(img, f"{confidence:.0f}%", (x1, y1))


            #CLASS NAME METHOD
            cls=int(box.cls[0])
            print(classNames[cls])
            cvzone.putTextRect(img, f"{classNames[cls]} {confidence:.2f}", (x1, y1))




    cv2.imshow("Video", img)
    cv2.waitKey(1)

