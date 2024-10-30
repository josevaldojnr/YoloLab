import cv2
import torch
import warnings

# Ignore future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load YOLOv5 model (YOLOv5s is a small model that’s faster but slightly less accurate)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Open the camera (0 is typically the default camera, change if using external)
cap = cv2.VideoCapture('http://192.168.1.16:4747/video')

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'q' to quit the video.")

# Run loop to capture frames and detect objects
while cap.isOpened():
    # Capture a frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Run YOLOv5 model on the frame
    results = model(frame)

    # Print detected objects
    detected_objects = results.xyxy[0]  # Get detections (x1, y1, x2, y2, conf, class)
    if len(detected_objects) > 0:
        for obj in detected_objects:
            # Extract class ID and confidence
            class_id = int(obj[5])  # The class index
            confidence = obj[4].item()  # The confidence score
            class_name = model.names[class_id]  # Get class name from index
            
            # Print detected object information
            print(f"Detected: {class_name}, Confidence: {confidence:.2f}")

    # Render results on the frame
    frame = results.render()[0]  # results.render() returns a list of images; [0] takes the first one

    # Display the frame with detections
    cv2.imshow("YOLOv5 Object Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
