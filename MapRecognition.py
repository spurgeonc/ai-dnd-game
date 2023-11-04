import cv2
import numpy as np
import string
import csv
import json

def label_cells(image_path, output_format='csv'):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Find contours of the grids
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours by their y-coordinate (top to bottom), and then by x-coordinate (left to right)
    contours = sorted(contours, key=lambda contour: (cv2.boundingRect(contour)[1], cv2.boundingRect(contour)[0]))

    labeled_cells = {}
    label_index = 0

    for idx, contour in enumerate(contours):
        if cv2.contourArea(contour) > 100:  # Adjust this threshold as needed
            # Calculate the centroid of the cell
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # Generate a unique cell label
                cell_label = f'{string.ascii_uppercase[label_index % 26]}{label_index // 26 + 1}'
                label_index += 1
                labeled_cells[f'Cell {idx + 1}'] = cell_label

                # Calculate the position to draw the label within the cell
                label_position = (cX - 15, cY + 15)  # Adjust these values as needed

                # Draw the label on the image
                cv2.putText(image, cell_label, label_position,
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Save the labeled image
    cv2.imwrite('labeled_map.png', image)

    if output_format == 'csv':
        # Export the labeled cells to a CSV file
        with open('labeled_cells.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Cell Number', 'Label'])
            for cell, label in labeled_cells.items():
                writer.writerow([cell, label])

    elif output_format == 'json':
        # Export the labeled cells to a JSON file
        with open('labeled_cells.json', 'w') as jsonfile:
            json.dump(labeled_cells, jsonfile, indent=4)

if __name__ == "__main__":
    input_image_path = 'map4.png'
    output_format = 'csv'  # Change to 'json' if you want JSON output
    label_cells(input_image_path, output_format)
