# Object-Detection-in-Rainy-Images-Project
Detection of objects in images containing rain using computer vision library after applying custom filter for deraining and using image processing concepts like gaussian blur, erosion and dilation, morphological operations etc..

This repository contains code to detect objects in rainy images. The main goal is to derain the image and identify objects, distinguishing between vertical and horizontal objects based on their aspect ratio.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Explanation of Key Steps](#explanation-of-key-steps)
- [Results](#results)

## Overview

This project aims to apply a simple deraining process on rainy images and detect objects by analyzing their contours. After preprocessing the image using filtering and morphological operations, we classify detected objects as either vertical or horizontal based on their aspect ratio.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/rainy-object-detection.git
    ```

2. Navigate to the project directory:
    ```bash
    cd rainy-object-detection
    ```

3. Ensure you have the required dependencies installed (see [Dependencies](#dependencies)).

## Usage

1. Place your rainy image in the project directory. Update the code to point to the correct image file if necessary:
    ```python
    rainy_image = cv2.imread('lotus_rainy.jpeg')  # Change this to your image
    ```

2. Run the Python script:
    ```bash
    python detect_objects.py
    ```

3. The program will display the detected objects in a window and print their labels (e.g., vertical or horizontal) in the terminal.

## Dependencies

Make sure to install the following libraries before running the script:

- OpenCV
- NumPy

You can install these dependencies using `pip`:

```bash
pip install opencv-python numpy
```

## Explanation of Key Steps

### Deraining the Image:
A simple deraining filter kernel is applied to reduce the rain effect using convolution.

```python
derain_kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
derained_image = cv2.filter2D(rainy_image, -1, derain_kernel)
```
## Preprocessing:
- The derained image is converted to grayscale.
- Gaussian blur is applied to reduce noise.
- Thresholding and morphological operations (erosion and dilation) help clean up the image for contour detection.

## Object Detection:
- Contours are found in the thresholded image.
- Objects are classified based on their aspect ratio. Horizontal objects have an aspect ratio > 1, while vertical objects have an aspect ratio ≤ 1.
- Bounding boxes and labels are drawn around detected objects.

```python
if aspect_ratio > 1.0:
    label = "Horizontal Object"
else:
    label = "Vertical Object"
```

## Displaying Results:
- The final image with bounding boxes and object labels is displayed, and the labels are printed to the console.

## Results

The following image shows the detected objects in the rainy image:

![Detected Objects](https://github.com/Bhavana9051/Object-Detection-in-Rainy-Images-Project/blob/main/Object%20Detection1.png?raw=true)

- Objects are detected based on their contours, and their orientation (vertical/horizontal) is classified.
- The processed image is displayed with bounding boxes around detected objects.

Example output:

```bash
Detected Objects: ['Vertical Object', 'Horizontal Object', ...]
```
