from PIL import Image
import os, time

def convert_png_to_bmp(png_file, bmp_file):
    """
    Converts a PNG image file to a BMP image file.
    """
    if not os.path.exists(png_file):
        print(f"Error: Source file '{png_file}' not found.")
        return

    try:
        # Open the PNG image
        img = Image.open(png_file)
        
        # BMP format does not support transparency. 
        # Convert to 'RGB' mode to handle potential alpha channel issues.
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            img = img.convert('RGB')
            print("Note: Converted image from RGBA/LA to RGB to remove transparency, as BMP does not support it well.")

        # Save the image as a BMP file
        img.save(bmp_file, 'BMP')
        print(f"Successfully converted '{png_file}' to '{bmp_file}'")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_file = os.environ.get('LINK')
output_file = f"{time.time()}.bmp"

# Create a dummy file for demonstration purposes if it doesn't exist
if not os.path.exists(source_file):
    print(f"'{source_file}' not found. Creating a sample PNG for demonstration.")
    # Create a simple red 100x100 RGB image with Pillow
    sample_img = Image.new('RGB', (100, 100), color = 'red')
    sample_img.save(source_file, 'PNG')

convert_png_to_bmp(source_file, output_file)
