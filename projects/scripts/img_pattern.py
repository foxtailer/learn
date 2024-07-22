import os
import sys
import shutil
from PIL import Image

def add_word_to_files(input_folder, output_folder, word="_pattern"):
    # Check if the input folder exists
    if not os.path.isdir(input_folder):
        print(f"Input folder '{input_folder}' does not exist.")
        return

    # Create the output folder if it does not exist
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        
        # Ensure it's a file
        if os.path.isfile(input_file_path):

            # Split the filename and its extension
            name, ext = os.path.splitext(filename)
            # Create the new filename by appending the word before the extension
            new_filename = f"{name}{word}{ext}"
            output_file_path = os.path.join(output_folder, new_filename)
            
            create_patterned_image(input_file_path, output_file_path)
            # Copy the file to the output folder with the new name
            #shutil.copy(input_file_path, output_file_path)
            
            print(f"Copied file: {filename} as {new_filename}")


def create_image_grid(input_image_path, output_image_path, n):
    # Open the input image
    base_image = Image.open(input_image_path)

    # Get the dimensions of the base image
    width, height = base_image.size

    # Create a new image with a size that can contain n x n copies of the base image
    new_image = Image.new('RGB', (width * n, height * n))

    # Paste the base image in the new image n x n times
    for row in range(n):
        for col in range(n):
            new_image.paste(base_image, (col * width, row * height))

    # Save the new image to the output path
    new_image.save(output_image_path)

def create_patterned_image(input_image_path, output_image_path):
     # Open the input image
    base_image = Image.open(input_image_path)

    # Get the dimensions of the base image
    width, height = base_image.size

    # Create a new image with a size that can contain the patterned layout
    # Convert dimensions to integers
    new_width = int(width * 3.3)
    new_height = int(height * 1.6)
    new_image = Image.new('RGB', (new_width, new_height))

    # Paste the base image in the new image with the pattern observed
    offsets = [
        (int(-width * 0.9), int(-height * 0.2)), 
        (int(width * 0.1), int(-height * 0.7)), 
        (int(width * 0.1 + width), int(-height * 0.2)), 
        (int(width * 0.1 + width * 2), int(-height * 0.7)), 
        (int(width * 0.1 + width * 3), int(-height * 0.2)), 
        (int(width * 0.1), int(height * 0.3)), 
        (int(width * 0.1 + width * 2), int(height * 0.3)), 
        (int(-width * 0.9), int(height * 0.8)), 
        (int(width * 0.1), int(height * 0.3 + height)), 
        (int(width * 0.1 + width), int(height * 0.8)), 
        (int(width * 0.1 + width * 2), int(height * 0.3 + height)), 
        (int(width * 0.1 + width * 3), int(height * 0.8))
    ]

    for (x_offset, y_offset) in offsets:
        new_image.paste(base_image, (x_offset, y_offset))

    # Save the new image to the output path
    new_image.save(output_image_path)

if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_folder> <output_folder> <word>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    word = sys.argv[3]

    add_word_to_files(input_folder, output_folder, word)
