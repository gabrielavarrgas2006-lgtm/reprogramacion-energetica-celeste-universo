import os
import math
from PIL import Image, ImageDraw

src_path = r'C:\Users\Gaby\.gemini\antigravity-ide\brain\6863dff8-7e74-44e5-b7ed-fa25194b89dd\.user_uploaded\media_1790152324930.jpg'
out_path = r'c:\Users\Gaby\Downloads\REPROGRAMACION ENERGETICA\logo.png'

im = Image.open(src_path).convert("RGBA")
width, height = im.size

# Find the circular mandala region or create a smooth circular mask
# The circular mandala is centered at (width/2, height/2) with radius ~470-490 px.
center_x, center_y = width / 2.0, height / 2.0

# Create mask with antialiasing (4x size then resize down)
mask_scale = 4
big_mask = Image.new("L", (width * mask_scale, height * mask_scale), 0)
draw = ImageDraw.Draw(big_mask)

# Radius estimation: circle boundary is at around r = 468 px (leaving out black corners)
radius = 468
bbox = [
    (center_x - radius) * mask_scale,
    (center_y - radius) * mask_scale,
    (center_x + radius) * mask_scale,
    (center_y + radius) * mask_scale
]
draw.ellipse(bbox, fill=255)

# Resize mask down to smooth edges
smooth_mask = big_mask.resize((width, height), Image.Resampling.LANCZOS)

# Create output RGBA image
result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
result.paste(im, (0, 0), smooth_mask)

# Also check for dark pixels around the edge and make them transparent if black
pix = result.load()
for x in range(width):
    for y in range(height):
        r, g, b, a = pix[x, y]
        # If pixel is near pure black (r < 25 and g < 25 and b < 25), set alpha = 0
        if r < 20 and g < 20 and b < 20:
            pix[x, y] = (0, 0, 0, 0)

result.save(out_path, "PNG")
print("Saved logo.png successfully with size:", result.size)
