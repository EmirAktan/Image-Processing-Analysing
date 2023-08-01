import cv2
import numpy as np
import random

def calculate_white_areas(image_path, pixel_area):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([179, 30, 255])
    mask = cv2.inRange(hsv_image, lower_white, upper_white)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    white_areas = []
    white_area_names = []
    # Create a copy of the original image to draw on
    image_with_white_areas = image.copy()
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        white_areas.append(area * pixel_area)
        white_area_names.append(str(i + 1))
        # Draw the contour on the image copy
        if area * pixel_area >= 100:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # White color  # White color
            image_with_white_areas = cv2.drawContours(image_with_white_areas, [contour], -1, color, 2)
            # Calculate the position for labeling
            moments = cv2.moments(contour)
            center_x = int(moments["m10"] / moments["m00"])
            center_y = int(moments["m01"] / moments["m00"])
            cv2.putText(image_with_white_areas, str(white_area_names[i]), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    return white_areas, white_area_names, image_with_white_areas  # Return the modified image


image_path = 'C:/Users/deneme/Desktop/png microglia overview.png'
pixel_area = (0.31991 * 0.31991)  

white_areas, white_area_names, image = calculate_white_areas(image_path, pixel_area)

# Print the surface area and name of each white area in microns squared
for i, area in enumerate(white_areas):
    if area >= 100:
        print(f"White area {white_area_names[i]}: {area} μm²")

cv2.imshow('Image with White Areas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



