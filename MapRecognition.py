import cv2
import pytesseract
from pytesseract import Output

# Load the image
image = cv2.imread('./maps/map1.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to enhance text contrast
ret, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours to detect individual cells or text regions
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize an empty list to store cell labels
cell_labels = []

# Loop through the detected contours
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    
    # Crop the cell region from the thresholded image
    cell_image = thresholded_image[y:y+h, x:x+w]
    
    # Use Tesseract to recognize the text in the cell
    cell_text = pytesseract.image_to_string(cell_image, config='--psm 6', output_type=Output.STRING)
    
    # Append the recognized text to the cell_labels list
    cell_labels.append(cell_text)

# Print the extracted cell labels
for idx, label in enumerate(cell_labels):
    print(f"Cell {idx + 1} Label: {label}")
