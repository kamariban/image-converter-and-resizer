# Image Converter and Resizer

## Overview
This is a simple Python script that converts images from one format to another. It can handle a single file or an entire folder of images, and also supports optional resizing.

---

## Features
- Convert between common formats (jpg, png, webp, etc.)
- Works on a single image or a whole directory
- Optional image resizing (set width and height)
- Automatically creates an output folder if it doesn’t exist

---

## Requirements
- Python 3.x
- Pillow library  

Install Pillow with:  
pip install pillow  

---

## Notes
- If width and height are provided, images will be resized before saving  
- If not provided, images are only converted  
- Only files matching the input format will be processed
