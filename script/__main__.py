from PIL import Image
import os

def convert_png_to_webp(input_folder, output_folder):
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            # Construct the full file paths
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.png', '.webp'))

            # Open the PNG image and convert it to WebP
            image = Image.open(input_path)
            image.save(output_path, 'WEBP')

            print(f'Converted {filename} to WebP')

if __name__ == '__main__':
    input_folder = 'images_png'
    output_folder = 'images_webp'
    convert_png_to_webp(input_folder, output_folder)

