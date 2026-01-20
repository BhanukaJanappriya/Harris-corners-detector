# Harris Corner Detection – OpenCV

This project presents an implementation, evaluation, and optimization of the **Harris Corner Detection** algorithm using **OpenCV**.  
The performance of the standard Harris detector is compared against an optimized version on structured patterns and natural scene images.

---
<img width="1500" height="500" alt="image5" src="https://github.com/user-attachments/assets/ebc57ee5-fab8-4edc-a884-72b385cbb594" />


## 📌 Project Overview

Corner detection is a fundamental task in computer vision, widely used in feature matching, object recognition, and image registration.  
This project explores how the Harris corner detector behaves under different image conditions and demonstrates how parameter tuning and preprocessing can significantly improve detection quality.

---

## 🔍 Key Features

- Standard Harris corner detection implementation
- Optimized Harris corner detection with:
  - Gaussian noise reduction
  - Parameter tuning
  - Sub-pixel corner refinement
- Visual comparison between normal and optimized outputs
- Evaluation on structured (chessboard) and natural scene images

---

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV**
- **NumPy**
- **Matplotlib**

---

## ⚙️ Methodology

### 1. Normal Harris Corner Detection
- Applied directly to grayscale images
- Detects corners using fixed parameters
- Sensitive to noise and texture in natural scenes

### 2. Optimized Harris Corner Detection
- Gaussian blur applied for noise reduction
- Increased block size and Sobel kernel for stability
- Thresholding to remove weak responses
- Sub-pixel refinement using `cv.cornerSubPix` for improved localization

---

## 🖼️ Results

The optimized Harris corner detector produces:
- Fewer false detections in textured regions
- Improved corner localization accuracy
- Cleaner and more interpretable corner distributions

Natural scenes benefit significantly from optimization, while structured images such as chessboards show consistently strong results in both approaches.

---

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/BhanukaJanappriya/harris-corner-detection-opencv.git
   ```

2. Install dependencies:
   ```bash
    pip install opencv-python numpy matplotlib
   ```

3. Run the script
   ```bash
    python src/optimized_harris_corner.py
   ```

---

## 📈 Applications

*Feature detection and matching

*Image registration

*Object recognition

*Computer vision education and experimentation

---
## 🧠 Learning Outcomes

-Understanding of Harris corner detection theory

-Practical experience with OpenCV

-Parameter optimization for real-world images

-Visualization and analysis of computer vision algorithms

---
## 👤 Author

Bhanuka Janappriya

---


