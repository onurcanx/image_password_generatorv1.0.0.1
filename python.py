import cv2
import numpy as np
import hashlib

# Load image using OpenCV
def load_image(image_path):
    """
    Loads an image from the given path using OpenCV.

    :param image_path: str, path to the image file
    :return: numpy array, loaded image
    """
    image = cv2.imread(image_path)
    return image

# Calculate the average color of the image
def get_average_color(image):
    """
    Calculates the average RGB color of the input image.

    :param image: numpy array, the image loaded in OpenCV
    :return: numpy array, the average RGB values
    """
    avg_color_per_row = np.average(image, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    return avg_color

# Convert RGB values to hexadecimal string
def rgb_to_hex(rgb):
    """
    Converts RGB values to a hexadecimal color code.

    :param rgb: numpy array, RGB values
    :return: str, hex color code
    """
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

# Create a password based on the image's average color
def create_password_from_image(image_path):
    """
    Generates a password based on the average color of an image.
    The average color is converted to a hex code, and the hex code
    is hashed using SHA-256 to produce a secure password.

    :param image_path: str, path to the image file
    :return: str, the generated password hash
    """
    image = load_image(image_path)

    # Calculate the average color of the image
    avg_color = get_average_color(image)

    # Convert the average color to hex format
    avg_color_hex = rgb_to_hex(avg_color)

    # Create a password hash using SHA-256
    password = hashlib.sha256(avg_color_hex.encode()).hexdigest()

    return password

# Example usage
if __name__ == "__main__":
    image_path = "6.png"  # Specify the image file path
    password = create_password_from_image(image_path)
    print(f"Generated Password: {password}")
