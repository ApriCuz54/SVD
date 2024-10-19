# Image Compression using Singular Value Decomposition (SVD)

This project demonstrates how **Singular Value Decomposition (SVD)** can be applied to compress images by reducing the rank of their matrix representation. SVD helps in retaining the most important features of an image while discarding less significant data, effectively reducing the image's size.

## Repo Structure:
- **`compress.py`**: Contains the implementation of SVD for image compression. The script allows setting different rank limits to observe how much data can be discarded while maintaining image quality.
- **`images`**: Directory containing:
  - The original images.
  - Compressed versions of the images with different rank limits to showcase the effect of SVD on image quality.

## How It Works:
1. The image is represented as a matrix where each pixel value is an element.
2. **SVD** is applied to decompose this matrix into three smaller matrices.
3. By adjusting the rank (number of singular values used), we can reduce the image size while preserving its essential features.
4. Higher rank retains more detail, while a lower rank results in greater compression but lower quality.

## Usage:
- Run the `compress.py` script to apply SVD to images in the `images/` directory.
- Experiment with different rank limits to see the trade-off between image quality and compression.

## Key Takeaway:
SVD-based image compression offers a powerful way to reduce image sizes while maintaining acceptable visual quality, demonstrating how mathematical techniques can be applied in practical image processing tasks.