from PIL import Image
import os

def convert_to_webp(input_folder, output_folder):
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is an image supported by PIL
        try:
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')

            # Open the image and convert it to WebP
            image = Image.open(input_path)
            image.save(output_path, 'WEBP')

            print(f'Converted {filename} to WebP')
        except IOError:
            print(f'Skipped {filename}, not a supported image file')

if __name__ == '__main__':
    input_folder = 'images'
    output_folder = 'images_webp'
    convert_to_webp(input_folder, output_folder)


