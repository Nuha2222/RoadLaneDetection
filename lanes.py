import cv2
import numpy as np

def canny(lane_image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) 
    canny = cv2.Canny(blur, 50, 150) # outline strongest gradients in image
    return canny

# image can be read as an array of pixels
def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
    [(200, height ), (1100, height), (550, 250)]
    ])
    mask = np.zeros_like(image) # same amount of pixels and dimensions as canny image
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask) # masking the canny image to show the region of interest
    return masked_image

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny_image = canny(lane_image)
cropped_image = region_of_interest(canny_image)
lines = cv2.HoughLines(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5)
cv2.imshow("result", cropped_image)
cv2.waitKey(0)
