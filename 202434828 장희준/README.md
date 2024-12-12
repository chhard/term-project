## README.md

---

### Project Overview
This project utilizes **computer vision** to calculate vehicle speed on roads and count the number of vehicles crossing a specific point in real time.  
It aims to address traffic management challenges such as **traffic flow analysis**, **speed limit violation detection**, and **road condition monitoring**.

---

### Demo and Example
#### Example Output
![opensource result](https://github.com/user-attachments/assets/59d2744e-7411-4d6f-9dfa-045235b3fa6d)
![opensouce result2](https://github.com/user-attachments/assets/b06c589d-227d-4e31-a693-76ea4cc5cab5)



---

### Dependencies and Required Files
This project requires the following:

#### Python Libraries
1. **OpenCV**
2. **NumPy**

#### YOLO Model Files
1. `yolov3.cfg`: YOLOv3 configuration file.
2. `yolov3.weights`: Pre-trained YOLOv3 weights file.
3. `coco.names.txt`: Text file containing class names.

These files can be downloaded from the official YOLO website or similar resources.

#### Input Video
An input video file (`trapic video.mp4`) to analyze vehicle movements.

---

### How to Run
1. **Prepare YOLO Files**
   - Place `yolov3.cfg`, `yolov3.weights`, and `coco.names.txt` in the project directory.

2. **Set Up Input Video**
   - Ensure that the input video (`trapic video.mp4`) is located in the same directory or update the file path in the script.

3. **Run the Script**
   - Save the provided Python code into a file named `vehicle_detection.py`.
   - Execute the script using:
     ```bash
     python vehicle_detection.py
     ```

4. **View Results**
   - The system will process the video, detect vehicles, and count those crossing the defined line in real time. And code will output the traffic congestion according to the number of vehicles.

---

### References
1. YOLOv3: [https://pjreddie.com/darknet/yolo/](https://pjreddie.com/darknet/yolo/)
2. OpenCV Documentation: [https://opencv.org/](https://opencv.org/)
3. COCO Names File: [https://github.com/pjreddie/darknet/blob/master/data/coco.names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)
4. Assistance and code structure provided by **GPT (ChatGPT)**: [https://gptonline.ai/](https://gptonline.ai/)

---

