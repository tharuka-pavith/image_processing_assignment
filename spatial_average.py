"""
This module provides a function for spatial averaging.

Author: Tharuka Pavith
"""
from PIL import Image, ImageFilter


def spatial_average(image_path, neighborhood_size) -> Image:
    """Performs spatial averaging on an image with a given kernel size.

      Args:
          image_path: Path to the image file.
          neighborhood_size: The size of the averaging kernel (e.g., 3, 10, 20).

      Returns:
          A new PIL Image object with the averaged image.
      """
    img = Image.open(image_path)
    img_avg = img.filter(ImageFilter.BoxBlur(neighborhood_size))
    return img_avg


if __name__ == '__main__':

    img = "girl.jpg"
    img1 = spatial_average(img, 3)  # 3x3 neighborhood
    img1.save("1.jpg")
    img2 = spatial_average(img, 10)  # 10x10 neighborhood
    img2.save("2.jpg")
    img3 = spatial_average(img, 20)  # 20x20 neighborhood
    img3.save("3.jpg")
