# OPEN CV BLUEPRINT
IAAC-MRAC-01_Hardware-II_February 2025


INTRODUCTION :

This repo is used for IAAC students and faculty to learn Python and OpenCV through projects. The concepts and tools learned through these projects are fundamental for future python and opencv development. This repo is designed for the preparation of MRAC students as they are entering the second term of the MRAC programme which is dedicated to sensing.

DESCRIPTION:

This project introduces architecture students to the basics of OpenCV through a practical exercise in image processing. The program processes blueprint images, highlights walls and room boundaries, and calculates areas of detected rooms. It’s designed for beginners to learn Python and OpenCV while applying programming skills to an architecture-related task.

 🎯 LEARNING OBJECTIVES :

By completing this exercise, students will:

 🎯Learn the basics of OpenCV for image processing.
 🎯Understand how to load, display, and manipulate images in Python.
 🎯Use edge detection and contour analysis to extract shapes from images.
 🎯Perform calculations like area measurement based on image data. Room Image Analysis with OpenCV

This project uses OpenCV and Matplotlib to process and analyze room images for various features, such as edge detection, contour detection, and area calculation.


FEATURES:

✅ LOAD & DISPLAY BLUEPRINT 
Load the image and display it in RGB format.
Load the image file from a specified path.
Convert the image to RGB format for accurate display.
Show the image using Matplotlib to visualize the blueprint.

✅ CONVERT TO GRAYSCALE
Convert the image to grayscale for easier processing.
Convert the original image to grayscale for simpler processing.
Reduce color complexity, focusing on intensity.
Prepare the image for edge detection by removing color variations.

✅ EDGE DETECTION
Use Gaussian Blur and Canny Edge Detection to highlight edges in the image.
Apply Gaussian Blur to smooth out noise in the image.
Use Canny Edge Detection to identify the boundaries of objects.
Highlight the edges to detect structural lines in the image.

✅ CONTOUR DETECTION
Detect contours in the image using thresholding and findContours.
Convert the image to binary through thresholding.
Detect contours that outline significant features in the image.
Draw contours on the image to visually mark boundaries.

✅ CALCULATE ROOM AREAS
Calculate and print the areas of detected contours, representing rooms.
Calculate the area of each detected contour in pixels.
Ignore small contours that don't represent significant features.
Print the areas of detected "rooms" in square pixels for further analysis.

 🎓 REFERENCES + ACKNOWLEDGEMENTS :

https://github.com/MRAC-IAAC/learn-python-with-this-project/blob/main/PYTHON-PROJECT.md

Marita Georganta) and Huanyu Li Instructors Creation of GitHub template: Marita Georganta - Robotic Sensing Expert Creation of MRAC-IAAC GitHub Structure: Huanyu Li - Robotic Researcher

Image Source:
https://thesefourwallsblog.com/how-to-plan-a-room-layout/
