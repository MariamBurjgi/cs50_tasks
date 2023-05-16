import sys
import os.path
from PIL import Image, ImageOps

# Check if exactly two command-line arguments were provided
if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py input.jpg output.jpg")

# Get the input and output file names
input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the file extensions are valid
valid_extensions = {'.jpg', '.jpeg', '.png'}
input_ext = os.path.splitext(input_file)[1].lower()
output_ext = os.path.splitext(output_file)[1].lower()
if input_ext not in valid_extensions or output_ext not in valid_extensions:
    sys.exit("Input and output files must have a .jpg, .jpeg, or .png extension")

# Check if the file extensions are the same
if input_ext != output_ext:
    sys.exit("Input and output files must have the same extension")

# Check if the input file exists
try:
    with open(input_file):
        pass
except FileNotFoundError:
    sys.exit("Input file does not exist")

# Open the input image and the shirt image
input_image = Image.open(input_file)
shirt_image = Image.open("shirt.png")

# Resize and crop the input image to the same size as the shirt image
input_image = ImageOps.fit(input_image, shirt_image.size)

# Overlay the shirt image on the input image
input_image.paste(shirt_image, (0, 0), shirt_image)

# Save the resulting image as the output file
input_image.save(output_file)
