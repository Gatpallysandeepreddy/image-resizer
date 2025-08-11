from resize_utils import resize_images

if __name__ == "__main__":
    input_folder = "images"        # Folder with original images
    output_folder = "resized"      # Folder where resized images will be saved
    size = (800, 600)              # New size
    format = "JPEG"                # Output format

    resize_images(input_folder, output_folder, size, format)
