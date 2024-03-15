"""
Main module for the image processing application

Author: Tharuka Pavith
"""
import tkinter as tk
from image_processing_app import ImageProcessingApp

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")  # Set window size to 400x500 pixels
    app = ImageProcessingApp(root)
    root.mainloop()
