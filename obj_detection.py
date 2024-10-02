import cv2
import numpy as np

# Load the rainy image
rainy_image = cv2.imread('lotus_rainy.jpeg')

# Define a deraining filter kernel
derain_kernel = np.array([[1, 2, 1],
                           [2, 4, 2],
                           [1, 2, 1]]) / 16

# Apply the deraining filter to the rainy image
derained_image = cv2.filter2D(rainy_image, -1, derain_kernel)

# Convert the derained image to grayscale for simpler processing
gray_image = cv2.cvtColor(derained_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Thresholding to create a binary mask
_, thresholded_image = cv2.threshold(blurred_image, 120, 255, cv2.THRESH_BINARY)

# Apply morphological operations (erosion and dilation) to improve object boundaries (Opening is done)
kernel = np.ones((5, 5), np.uint8)
thresholded_image = cv2.erode(thresholded_image, kernel, iterations=1)
thresholded_image = cv2.dilate(thresholded_image, kernel, iterations=1)

# Find contours in the binary mask
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize a list to store detected objects
detected_objects = []

# Draw bounding boxes around detected objects and label them
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    
    # Filter out small contours to remove noise
    if cv2.contourArea(contour) > 100:
        # Get the aspect ratio to differentiate between vertical and horizontal objects
        aspect_ratio = float(w) / h
        if aspect_ratio > 1.0:
            label = "Horizontal Object"
        else:
            label = "Vertical Object"
        
        detected_objects.append(label)
        
        # Draw bounding box with label
        cv2.rectangle(derained_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(derained_image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


print("Detected Objects:", detected_objects)

# Display the result
cv2.imshow('Object Detection', derained_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

