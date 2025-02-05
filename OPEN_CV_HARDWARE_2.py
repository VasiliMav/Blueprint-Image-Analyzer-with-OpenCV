# IMPORT LIBRARIES

import cv2  # Import OpenCV for image processing
import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for displaying images
import os  # Import OS to handle file paths

# FUNCTION TO DISPLAY IMAGE

def SHOW_IMAGE(IMAGE, TITLE="Image", CMAP=None):
    plt.imshow(IMAGE, cmap=CMAP)
    plt.title(TITLE)
    plt.axis("off")
    plt.show()

# SET IMAGE PATH FROM GITHUB REPOSITORY

IMAGE_PATH = "open_cv_example.jpg"  # Adjust path to the folder of the Github repository

# CHECK IF IMAGE EXISTS

if not os.path.exists(IMAGE_PATH):
    print(f"ERROR: The file does not exist at '{IMAGE_PATH}'")
    exit()
else:
    print("Great. File found!")

# FEATURES

# 1.LOAD & DISPLAY BLUEPRINT
# 2.CONVERT TO GRAYSCALE
# 3.EDGE DETECTION
# 4.CONTOUR DETECTION
# 5.CALCULATE ROOM AREAS

# STEP 1: LOAD AND DISPLAY IMAGE
IMAGE = cv2.imread(IMAGE_PATH)  # Load the image
if IMAGE is None:
    print("Error: Could not load image. Check file format or path.")
    exit()

IMAGE_RGB = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2RGB)  # Convert to RGB for Matplotlib
SHOW_IMAGE(IMAGE_RGB, TITLE="Original Image")

# STEP 2: CONVERT TO GRAYSCALE
GRAY = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
SHOW_IMAGE(GRAY, TITLE="Grayscale Image", CMAP="gray")

# STEP 3: EDGE DETECTION
BLUR = cv2.GaussianBlur(GRAY, (5, 5), 0)  # Apply Gaussian Blur
EDGES = cv2.Canny(BLUR, 100, 200)  # Use Canny Edge Detection
SHOW_IMAGE(EDGES, TITLE="Edge Detection", CMAP="gray")

# STEP 4: CONTOUR DETECTION
BLUR_FOR_CONTOURS = cv2.GaussianBlur(GRAY, (5, 5), 0)  # Reduce noise before thresholding
_, BINARY = cv2.threshold(BLUR_FOR_CONTOURS, 50, 255, cv2.THRESH_BINARY)  # Convert to binary
CONTOURS, _ = cv2.findContours(BINARY, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Detect contours
IMAGE_CONTOURS = cv2.drawContours(IMAGE.copy(), CONTOURS, -1, (0, 255, 0), 2)  # Draw contours
SHOW_IMAGE(cv2.cvtColor(IMAGE_CONTOURS, cv2.COLOR_BGR2RGB), TITLE="Detected Contours")

# STEP 5: CALCULATE ROOM AREAS
for I, CNT in enumerate(CONTOURS):
    AREA = cv2.contourArea(CNT)  # Calculate contour area
    if AREA > 100:  # Ignore small areas
        print(f"Room {I}: {AREA:.2f} square pixels")

# STEP 6: UNIT CONVERSION
def CONVERT_AREA(PIXEL_AREA, SCALE):
    return PIXEL_AREA * (SCALE ** 2)  # Convert pixel area to real-world units

# HANDLE USER INPUT SAFELY
while True:
    try:
        SCALE = float(input("Enter real-world length of one pixel (e.g., in feet): "))
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

for I, CNT in enumerate(CONTOURS):
    PIXEL_AREA = cv2.contourArea(CNT)
    if PIXEL_AREA > 100:
        REAL_AREA = CONVERT_AREA(PIXEL_AREA, SCALE)
        print(f"Room {I}: {REAL_AREA:.2f} square units")
