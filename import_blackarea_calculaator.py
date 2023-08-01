import cv2
import numpy as np
import random

def calculate_black_areas(image_path, pixel_area):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([179, 30, 255])
    mask_white = cv2.inRange(hsv_image, lower_white, upper_white)

    # Create the mask for black areas by inverting the white mask
    mask_black = cv2.bitwise_not(mask_white)

    contours, _ = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    black_areas = []
    black_area_names = []
    
    image_with_black_areas = image.copy()
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        black_areas.append(area * pixel_area)
        black_area_names.append(str(i + 1))
        
        if area * pixel_area >= 100:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Black color
            image_with_black_areas = cv2.drawContours(image_with_black_areas, [contour], -1, color, 2)
            
            moments = cv2.moments(contour)
            center_x = int(moments["m10"] / moments["m00"])
            center_y = int(moments["m01"] / moments["m00"])
            cv2.putText(image_with_black_areas, str(black_area_names[i]), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    return black_areas, black_area_names, image_with_black_areas  # Return the modified image


image_path = 'C:/Users/deneme/Desktop/classification_result_microglia.png'
pixel_area = (0.3126 * 0.3126)  

black_areas, black_area_names, image = calculate_black_areas(image_path, pixel_area)


for i, area in enumerate(black_areas):
    if area >= 100:
        print(f"Black area {black_area_names[i]}: {area} μm²")

cv2.imshow('Image with Black Areas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
