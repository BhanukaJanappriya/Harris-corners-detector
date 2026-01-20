import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Load image
# --------------------------------------------------
filename = 'image2.jpg'
img = cv.imread(filename)
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_f32 = np.float32(gray)

# ==================================================
# NORMAL HARRIS CORNER DETECTION
# ==================================================
dst_normal = cv.cornerHarris(gray_f32, 2, 3, 0.04)
dst_normal = cv.dilate(dst_normal, None)

img_normal = img.copy()
img_normal[dst_normal > 0.01 * dst_normal.max()] = [0, 0, 255]
img_normal_rgb = cv.cvtColor(img_normal, cv.COLOR_BGR2RGB)


# Preprocessing
gray_blur = cv.GaussianBlur(gray, (5, 5), 0)
gray_blur_f32 = np.float32(gray_blur)

dst_opt = cv.cornerHarris(gray_blur_f32, 4, 5, 0.05)
dst_opt = cv.dilate(dst_opt, None)

# Thresholding
_, dst_thresh = cv.threshold(
    dst_opt,
    0.01 * dst_opt.max(),
    255,
    0
)
dst_thresh = np.uint8(dst_thresh)

# Connected components
_, labels, stats, centroids = cv.connectedComponentsWithStats(dst_thresh)

# Sub-pixel refinement
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv.cornerSubPix(
    gray_blur_f32,
    np.float32(centroids),
    (5, 5),
    (-1, -1),
    criteria
)

# Draw optimized corners
img_opt = img.copy()
for c in corners:
    cv.circle(img_opt, (int(c[0]), int(c[1])), 1, (0, 255, 0), -1)

img_opt_rgb = cv.cvtColor(img_opt, cv.COLOR_BGR2RGB)


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(img_normal_rgb)
plt.title("Normal Harris Output")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(img_opt_rgb)
plt.title("Optimized Harris Output")
plt.axis('off')

plt.tight_layout()
plt.show()
