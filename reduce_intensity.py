"""
This module provides a function to reduce intensity level.

Author: Tharuka Pavith
"""

import numpy as np
from PIL import Image


def reduce_intensity_levels(image_path, num_levels):
    """Reduces the number of intensity levels in an image.

  Args:
      image_path: Path to the image file.
      num_levels: Desired number of intensity levels (must be a power of 2).

  Returns:
      A PIL Image object with the reduced intensity levels.
  """

    if not (num_levels & (num_levels - 1) == 0):
        raise ValueError("Number of intensity levels must be a power of 2")

    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img_data = np.array(img)
    max_intensity = 255 // (num_levels - 1)  # Calculate new intensity range

    # Apply thresholding to reduce intensity levels
    reduced_img = np.zeros_like(img_data)
    for i in range(img_data.shape[0]):
        for j in range(img_data.shape[1]):
            reduced_img[i, j] = (img_data[i, j] // max_intensity) * max_intensity

    return Image.fromarray(reduced_img.astype(np.uint8))


if __name__ == "__main__":

    image_path = "girl.jpg"
    num_levels = 8  # Change this to desired number of levels (power of 2)
    reduced_image = reduce_intensity_levels(image_path, num_levels)
    reduced_image.save("reduced_image.jpg")
