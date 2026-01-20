import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Read image
img = cv.imread('image1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Create SIFT detector
sift = cv.SIFT_create()
kp = sift.detect(gray, None)

# Draw keypoints
img_kp = cv.drawKeypoints(
    gray, kp, None,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# Plot using matplotlib
plt.figure(figsize=(8, 8))
plt.imshow(img_kp, cmap='gray')
plt.title('SIFT Keypoints')
plt.axis('off')
plt.show()
