from PIL import Image, ImageDraw, ImageFilter
import numpy as np

def create_sketch_background(width, height):
    # Create a blank image with white background
    img = Image.new('L', (width, height), 255)
    draw = ImageDraw.Draw(img)

    # Draw random lines to simulate pencil sketch
    for i in range(20000):  # Adjust the range for more or less lines
        x1, y1 = np.random.randint(0, width), np.random.randint(0, height)
        x2, y2 = x1 + np.random.randint(-20, 20), y1 + np.random.randint(-20, 20)
        draw.line((x1, y1, x2, y2), fill=np.random.randint(0, 255), width=1)

    # Apply a blur filter to soften the lines
    img = img.filter(ImageFilter.GaussianBlur(1))

    return img

# Create the sketch background
width, height = 512, 512
sketch_bg = create_sketch_background(width, height)

# Save the image
sketch_bg.save("/Documents/python/sketch_background.png")
