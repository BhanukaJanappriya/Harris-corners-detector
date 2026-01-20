import numpy as np
import cv2 as cv
filename = 'super_zoomed.png'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()










# import numpy as np
# import cv2 as cv

# # ============================================
# # APPROACH 1: Basic Optimized Harris Corner
# # ============================================
# def optimized_harris_basic(filename):
#     """Most straightforward optimization - removes unnecessary operations"""
#     img = cv.imread(filename)
#     if img is None:
#         print(f"Error: Could not read image {filename}")
#         return

#     # Direct conversion without float32
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#     # cornerHarris works with uint8 directly
#     dst = cv.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

#     # Mark corners without dilation
#     threshold = 0.01 * dst.max()
#     img[dst > threshold] = [0, 0, 255]

#     cv.imshow('Optimized Harris - Basic', img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()


# # ============================================
# # APPROACH 2: With Non-Maximum Suppression
# # ============================================
# def optimized_harris_nms(filename):
#     """Better corner localization using non-maximum suppression"""
#     img = cv.imread(filename)
#     if img is None:
#         print(f"Error: Could not read image {filename}")
#         return

#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     dst = cv.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

#     # Apply threshold
#     threshold = 0.01 * dst.max()
#     corner_mask = dst > threshold

#     # Non-maximum suppression for precise corner points
#     kernel = np.ones((5, 5), np.uint8)
#     local_max = cv.dilate(dst, kernel)
#     corner_mask = (dst == local_max) & corner_mask

#     # Mark corners
#     img[corner_mask] = [0, 0, 255]

#     cv.imshow('Optimized Harris - NMS', img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()


# # ============================================
# # APPROACH 3: Fast Processing (Downscaled)
# # ============================================
# def optimized_harris_fast(filename, scale=0.5):
#     """Faster processing for large images using downscaling"""
#     img = cv.imread(filename)
#     if img is None:
#         print(f"Error: Could not read image {filename}")
#         return

#     original_shape = img.shape

#     # Downscale for faster processing
#     small_img = cv.resize(img, None, fx=scale, fy=scale,
#                           interpolation=cv.INTER_AREA)
#     small_gray = cv.cvtColor(small_img, cv.COLOR_BGR2GRAY)

#     # Detect corners on smaller image
#     dst = cv.cornerHarris(small_gray, blockSize=2, ksize=3, k=0.04)
#     threshold = 0.01 * dst.max()
#     small_img[dst > threshold] = [0, 0, 255]

#     # Upscale back to original size
#     result = cv.resize(small_img, (original_shape[1], original_shape[0]),
#                        interpolation=cv.INTER_LINEAR)

#     cv.imshow('Optimized Harris - Fast', result)
#     cv.waitKey(0)
#     cv.destroyAllWindows()


# # ============================================
# # APPROACH 4: Using goodFeaturesToTrack
# # ============================================
# def optimized_shi_tomasi(filename, max_corners=100):
#     """Alternative using Shi-Tomasi (generally faster and more robust)"""
#     img = cv.imread(filename)
#     if img is None:
#         print(f"Error: Could not read image {filename}")
#         return

#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#     # Detect corners using Shi-Tomasi
#     corners = cv.goodFeaturesToTrack(gray,
#                                       maxCorners=max_corners,
#                                       qualityLevel=0.01,
#                                       minDistance=10,
#                                       blockSize=3)

#     # Draw corners
#     if corners is not None:
#         corners = np.int32(corners)
#         for corner in corners:
#             x, y = corner.ravel()
#             cv.circle(img, (x, y), 3, (255, 0, 0), -1)

#     cv.imshow('Optimized Shi-Tomasi', img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()


# # ============================================
# # APPROACH 5: Best Performance with Tuning
# # ============================================
# def optimized_harris_advanced(filename):
#     """Advanced optimization with parameter tuning"""
#     img = cv.imread(filename)
#     if img is None:
#         print(f"Error: Could not read image {filename}")
#         return

#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#     # Tuned parameters for better detection
#     dst = cv.cornerHarris(gray, blockSize=3, ksize=5, k=0.04)

#     # Adaptive threshold based on image statistics
#     threshold = 0.01 * dst.max()
#     corner_mask = dst > threshold

#     # Non-maximum suppression
#     kernel = np.ones((7, 7), np.uint8)
#     local_max = cv.dilate(dst, kernel)
#     corner_mask = (dst == local_max) & corner_mask

#     # Draw circles instead of just marking pixels
#     corner_coords = np.argwhere(corner_mask)
#     for coord in corner_coords:
#         cv.circle(img, (coord[1], coord[0]), 5, (0, 0, 255), 2)

#     cv.imshow('Optimized Harris - Advanced', img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()


# # ============================================
# # Main Execution
# # ============================================
# if __name__ == "__main__":
#     filename = 'image3.jpg'

#     # Choose which approach to run:
#     print("Running optimized Harris corner detection...")

#     # Uncomment the approach you want to use:
#     optimized_harris_basic(filename)
#     # optimized_harris_nms(filename)
#     # optimized_harris_fast(filename, scale=0.5)
#     # optimized_shi_tomasi(filename, max_corners=100)
#     # optimized_harris_advanced(filename)
