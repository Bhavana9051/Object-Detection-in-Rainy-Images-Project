import cv2

# Load the rainy image
rainy_image = cv2.imread('hand1_rainy.jpeg')

# Convert the image to grayscale for simpler processing
gray_image = cv2.cvtColor(rainy_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Thresholding to create a binary mask
_, thresholded_image = cv2.threshold(blurred_image, 120, 255, cv2.THRESH_BINARY)

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
        cv2.rectangle(rainy_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(rainy_image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the result
cv2.imshow('Object Detection', rainy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print detected objects
print("Detected Objects:", detected_objects)
