"""
This module provides a simple user interface for image processing.

Author: Tharuka Pavith
"""
from reduce_intensity import reduce_intensity_levels
from reduce_resolution import block_average
from rotate import rotate_image
from spatial_average import spatial_average

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk


class ImageProcessingApp:
    """
        A class representing a GUI for image processing application.

        This class provides a user interface for loading images, applying filters, and performing various image
        transformations.
        """
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")

        self.image = None
        self.image_path = ""

        # Create GUI elements
        self.label = tk.Label(root, text="Select an image:")
        self.label.pack()

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.process_label = tk.Label(root, text="Choose an operation:")
        self.process_label.pack()

        self.operations = [
            ("Reduce Intensity Levels", self.reduce_intensity_levels),
            ("Spatial Average (3x3)", lambda: self.spatial_average(3)),
            ("Spatial Average (10x10)", lambda: self.spatial_average(10)),
            ("Spatial Average (20x20)", lambda: self.spatial_average(20)),
            ("Rotate 45 Degrees", lambda: self.rotate_image(45)),
            ("Rotate 90 Degrees", lambda: self.rotate_image(90)),
            ("Average Blocks (3x3)", lambda: self.average_blocks(3)),
            ("Average Blocks (5x5)", lambda: self.average_blocks(5)),
            ("Average Blocks (7x7)", lambda: self.average_blocks(7))
        ]

        self.process_var = tk.StringVar()
        for text, command in self.operations:
            rb = tk.Radiobutton(root, text=text, variable=self.process_var, value=text)
            rb.pack(anchor=tk.W)

        self.process_button = tk.Button(root, text="Process", command=self.process_image)
        self.process_button.pack()

    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            # If there's an existing image label, destroy it
            if hasattr(self, 'img_label'):
                self.img_label.destroy()
            self.image = Image.open(self.image_path)
            self.image.thumbnail((300, 300))  # Resize image for display
            imgtk = ImageTk.PhotoImage(self.image)
            self.img_label = tk.Label(self.root, image=imgtk)
            self.img_label.image = imgtk
            self.img_label.pack()

    def reduce_intensity_levels(self):
        if self.image:
            num_levels = int(self.ask_num_levels())
            if not (num_levels & (num_levels - 1) == 0):
                messagebox.showerror("Invalid Intensity Level",
                                       "Intensity levels in an image should be from from 256 to 2, in integer "
                                       "powers of 2.")
            img = reduce_intensity_levels(self.image_path, num_levels)
            self.display_image(img)

    def spatial_average(self, neighborhood_size):
        if self.image:
            img_avg = spatial_average(self.image_path, neighborhood_size)
            self.display_image(img_avg)

    def rotate_image(self, angle):
        if self.image:
            img_rotated = rotate_image(self.image_path, angle)
            self.display_image(img_rotated)

    def average_blocks(self, block_size):
        if self.image:
            decimated_image = block_average(self.image_path, block_size)
            self.display_image(decimated_image)

    def process_image(self):
        selected_operation = self.process_var.get()
        if selected_operation:
            for text, command in self.operations:
                if text == selected_operation:
                    command()
                    break
        else:
            messagebox.showwarning("No Operation Selected", "Please select an operation to process the image.")

    def display_image(self, img):
        img.thumbnail((300, 300))  # Resize image for display
        imgtk = ImageTk.PhotoImage(img)
        self.img_label.configure(image=imgtk)
        self.img_label.image = imgtk

    def ask_num_levels(self):
        return simpledialog.askstring("Number of Intensity Levels", "Enter the number of intensity levels:")
