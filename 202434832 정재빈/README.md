# **Shape Detection with OpenCV**

### Detecting geometric shapes in images using OpenCV and Python

I worked by referring to the work of [OpenCV shape detection](https://pyimagesearch.com/2016/02/08/opencv-shape-detection/). I've included code modified from the author's code.

## **Key Features**
1. Detects geometric shapes (circle, triangle, square, rectangle, pentagon, hexagon) in an image.
2. Draws contours around the detected shapes.
3. Labels the shapes with their corresponding names.

## **How It Works**
1. **Image Preprocessing**:
   - The input image is resized for easier computation.
   - The resized image is converted to grayscale.
   - A Gaussian blur is applied to reduce noise.
   - The blurred image is thresholded to create a binary image, separating the foreground from the background.

2. **Contour Detection**:
   - Contours are detected using OpenCV's `findContours` function.
   - Each contour corresponds to a possible shape in the image.

3. **Shape Detection**:
   - The contours are analyzed to approximate their polygonal curves using OpenCV's `approxPolyDP` function.
   - Based on the number of vertices, the shape is identified:
     - **3 vertices**: Triangle
     - **4 vertices**: Square or Rectangle (based on aspect ratio)
     - **5 vertices**: Pentagon
     - **6 vertices**: Hexagon
     - **Other shapes**: Circle (default)

4. **Annotation**:
   - The contours are drawn on the original image.
   - The name of the detected shape is labeled at the center of each shape.

## **Requirements**
1. Python (>=3.7)
2. OpenCV (>=4.1.0)
3. imutils (>=0.5.2)

## **Running the Program**
1. Place your image at the specified path (e.g., `./image/shapes_and_colors.png`).
2. Ensure that the `pyimagesearch` file is located in the same directory as the `detect_shapes.py` script.
3. Run the code using Python.
4. The output image will display the detected shapes with their names.


## **Example Output**
The program processes an input image containing shapes of different types and outputs the same image with contours and labels.

## **The limitations
1. Only flat shapes can be recognized accurately.
2. As the number of vertices increases, it may become indistinguishable from a circle.
---
