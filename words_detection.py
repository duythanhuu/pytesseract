import cv2
import pytesseract
import os
from pytesseract import Output

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Path to the images folder
images_folder_path = 'images'

# Get a list of all files in the images folder
image_files = os.listdir(images_folder_path)

# Loop through each image file
for image_file in image_files:
    # Construct the full image path
    image_path = os.path.join(images_folder_path, image_file)

    # Read the image
    image = cv2.imread(image_path)

    # Perform OCR on the image
    d = pytesseract.image_to_data(image, output_type=Output.DICT)

    # Get the number of words detected
    n_boxes = len(d['level'])

    # Loop through each word and draw a bounding box around it
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Print the position of each detected word
        print(f"Word: {d['text'][i]} | Position: ({x}, {y}, {w}, {h})")

    # Display the image with bounding boxes
    cv2.imshow('Image with Bounding Boxes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()