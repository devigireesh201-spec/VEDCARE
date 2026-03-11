"""
Fix plant images: replace checkerboard/white/gray background with #f0fdf4 (circle bg color).
Uses Pillow to detect and replace near-white/gray pixels.
"""
from PIL import Image
import os

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
IMAGE_FILES = ['plant_1.png', 'plant_2.png', 'plant_3.png']

# Target background color (the circle's bg: #f0fdf4)
BG_COLOR = (240, 253, 244, 255)  # RGBA

# Threshold: pixels brighter than this (in all channels) are considered background
BRIGHTNESS_THRESHOLD = 200
GRAY_SIMILARITY_THRESHOLD = 25  # Max diff between R, G, B to be "gray"

def is_background_pixel(r, g, b, a=255):
    """Return True if the pixel looks like a checkerboard (gray or white) background."""
    # Transparent pixels
    if a < 128:
        return True
    # Light gray or white pixels (checkerboard = alternating light/dark grays)
    # Check if R, G, B are all similar (grayish) and fairly bright
    max_rgb = max(r, g, b)
    min_rgb = min(r, g, b)
    is_grayish = (max_rgb - min_rgb) < GRAY_SIMILARITY_THRESHOLD
    is_light = min_rgb > 160  # All channels above 160 = fairly light
    return is_grayish and is_light

def process_image(filepath):
    img = Image.open(filepath).convert('RGBA')
    data = img.load()
    width, height = img.size
    
    replaced = 0
    for y in range(height):
        for x in range(width):
            pixel = data[x, y]
            r, g, b, a = pixel
            if is_background_pixel(r, g, b, a):
                data[x, y] = BG_COLOR
                replaced += 1
    
    img.save(filepath, 'PNG')
    print(f"  Processed {os.path.basename(filepath)}: replaced {replaced} background pixels")

print("Fixing plant images...")
for filename in IMAGE_FILES:
    filepath = os.path.join(STATIC_DIR, filename)
    if os.path.exists(filepath):
        process_image(filepath)
    else:
        print(f"  SKIPPED {filename} (not found)")

print("\nDone! All plant images processed.")
