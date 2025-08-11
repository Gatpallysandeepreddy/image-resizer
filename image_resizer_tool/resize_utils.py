import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 600), format="JPEG"):
    """
    Resize and convert all images in a folder.

    Args:
        input_folder (str): Path to input images.
        output_folder (str): Path to save resized images.
        size (tuple): New size (width, height).
        format (str): Output format (JPEG, PNG, etc.).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        try:
            with Image.open(file_path) as img:
                img = img.resize(size)
                base_name, _ = os.path.splitext(filename)
                save_path = os.path.join(output_folder, f"{base_name}.{format.lower()}")
                img.save(save_path, format=format)
                print(f"✅ Resized & saved: {save_path}")
        except Exception as e:
            print(f"❌ Skipped {filename}: {e}")
