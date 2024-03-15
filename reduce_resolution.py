"""
This module provides a function to reduce resolution.

Author: Tharuka Pavith
"""
import numpy as np
from PIL import Image


def block_average(image_path, block_size) -> Image:
    """Reduces image resolution by averaging pixels in blocks.

  Args:
      image_path: Path to the image file.
      block_size: The size of the block for averaging (e.g., 3, 5, 7).

  Returns:
      A new PIL Image object with the decimated image.
  """

    im = np.array(Image.open(image_path))
    height, width = im.shape[:2]  # Get image height and width

    # Calculate the output image dimensions considering padding
    new_height = (height + block_size - 1) // block_size
    new_width = (width + block_size - 1) // block_size

    # Calculate padding required for perfect block division
    pad_height = (new_height - 1) * block_size - height
    pad_width = (new_width - 1) * block_size - width

    # Check if padding is needed
    if pad_height > 0 or pad_width > 0:
        # Pad the image with constant values (e.g., 0 for black)
        pad_values = ((0, pad_height), (0, pad_width))  # Padding for top/bottom, left/right
        if len(im.shape) == 3:  # Color image
            pad_values = pad_values + ((0, 0),)  # Padding for color channels
        im = np.pad(im, pad_values, mode='constant')

    # Create empty NumPy array for the decimated image
    averaged_image = np.zeros((new_height, new_width), dtype=im.dtype)

    for y in range(new_height):
        for x in range(new_width):
            # Extract block of pixels from padded image, handling potential edge cases
            start_y = min(y * block_size, height)
            end_y = min((y + 1) * block_size, height + pad_height)
            start_x = min(x * block_size, width)
            end_x = min((x + 1) * block_size, width + pad_width)
            block = im[start_y:end_y, start_x:end_x]

            # Check for empty block (entirely outside image) and skip averaging
            if block.size == 0:
                continue

            # Calculate average of the block (avoiding division by zero)
            averaged_pixel = np.mean(block) if block.size > 0 else 0  # Handle empty block

            # Set the corresponding pixel in the decimated image
            averaged_image[y, x] = averaged_pixel

    return Image.fromarray(averaged_image.astype(np.uint8))


if __name__ == '__main__':

    image_path = "girl.jpg"
    block_sizes = [3, 5, 7]
    for block_size in block_sizes:
        decimated_image = block_average(image_path, block_size)
        decimated_image.save(f"decimated_{block_size}x{block_size}.jpg")
