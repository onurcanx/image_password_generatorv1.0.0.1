# Image-Based Password Generator

This Python project generates a secure password based on the average color of an image. The password is created by calculating the average color of an image, converting the color to a hexadecimal format, and then hashing it using the SHA-256 algorithm.

## Features

- Loads an image using OpenCV.
- Calculates the average RGB color of the image.
- Converts the average color to a hex format.
- Generates a password hash from the hex color using SHA-256.

## Prerequisites

To run this project, you need Python 3 installed along with the following Python libraries:

- OpenCV
- NumPy
- Pillow

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
