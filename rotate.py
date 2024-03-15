"""
This module provides a function to rotate image.

Author: Tharuka Pavith
"""
from PIL import Image


def rotate_image(image_path, angle) -> Image:
    """Rotates an image by the specified angle.

  Args:
      image_path: Path to the image file.
      angle: The rotation angle in degrees (e.g., 45, 90).

  Returns:
      A new PIL Image object with the rotated image.
  """

    im = Image.open(image_path)
    rotated_image = im.rotate(angle)
    return rotated_image


if __name__ == '__main__':

    image_path = "girl.jpg"
    angles = [45, 90]
    for angle in angles:
        rotated_image = rotate_image(image_path, angle)
        rotated_image.save(f"rotated_{angle}deg.jpg")
