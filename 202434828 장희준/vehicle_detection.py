import cv2
import numpy as np
import time

# Define function to calculate speed
def calculate_speed(p1, p2, fps):
    distance_in_pixels = np.linalg.norm(np.array(p2) - np.array(p1))
    speed = distance_in_pixels * fps  # Pixels per second (conversion to real-world speed required)
    return speed

# Initialize video capture
video_path = 'trapic video.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Video not found or cannot be loaded.")
    exit()

fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Load YOLO model
net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

# Load class names
with open("coco.names.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Define output layers
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Variables for tracking
tracking_data = {}  # Store positions of detected vehicles
line_position = int(frame_height * 0.8)  # Define a horizontal line for counting vehicles
vehicle_count = 0

# Process each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    height, width, channels = frame.shape

    # Create blob from frame
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Detect objects
    class_ids = []
    confidence_scores = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and classes[class_id] == 'car':  # Detect only cars
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidence_scores.append(float(confidence))
                class_ids.append(class_id)

    indices = cv2.dnn.NMSBoxes(boxes, confidence_scores, 0.5, 0.4)

    # Draw bounding boxes and track objects
    for i in indices:
        x, y, w, h = boxes[i]
        center = (x + w // 2, y + h // 2)

        # Assign ID and track vehicle
        id_assigned = False
        for vehicle_id, positions in tracking_data.items():
            if np.linalg.norm(np.array(positions[-1]) - np.array(center)) < 50:  # Distance threshold
                tracking_data[vehicle_id].append(center)
                id_assigned = True
                break

        if not id_assigned:
            tracking_data[len(tracking_data)] = [center]

        # Check if the vehicle crosses the line
        for vehicle_id, positions in list(tracking_data.items()):
            if len(positions) > 1 and positions[-2][1] < line_position <= positions[-1][1]:
                vehicle_count += 1
                print(f"Vehicle {vehicle_id} crossed the line. Total count: {vehicle_count}")
                del tracking_data[vehicle_id]  # Stop tracking after crossing

        # Draw bounding box and line
        color = (0, 255, 0)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, f"ID {len(tracking_data)}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Draw the counting line
    cv2.line(frame, (0, line_position), (frame_width, line_position), (0, 0, 255), 2)

    # Display frame
    cv2.imshow("Vehicle Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"Total vehicles counted: {vehicle_count}")

if vehicle_count < 10:
    congestion_status = "traffic congestion: low"
elif 10 <= vehicle_count < 20:
    congestion_status = "traffic congestion: medium"
else:
    congestion_status = "traffic congestion: high"

print(f"traffic congestion: {congestion_status}")
