# Image Resizer

A simple Python tool for batch resizing and converting images in a folder.

## Features

- Resize all images in a given directory to a specified size
- Convert images to a desired format (e.g., JPEG, PNG)
- Saves resized images to an output folder
- Uses the popular [Pillow](https://python-pillow.org/) library

## Usage

1. Place your original images in the `images` folder (you can change this in the code).
2. Run the main script:

   ```bash
   python image_resizer_tool/main.py
   ```

   By default, images will be resized to 800x600 pixels and saved in JPEG format to the `resized` directory.

## Customization

You can modify the following variables in `main.py`:

- `input_folder`: Directory containing your original images
- `output_folder`: Directory to save resized images
- `size`: Desired output size (width, height)
- `format`: Output image format (e.g., "JPEG", "PNG")

## Requirements

- Python 3
- Pillow library

Install dependencies:

```bash
pip install Pillow
```

## Example

If you have several PNG images in the `images` folder, running the script will resize them to 800x600 JPEGs in the `resized` folder.

## Author

[Gatpallysandeepreddy](https://github.com/Gatpallysandeepreddy)
