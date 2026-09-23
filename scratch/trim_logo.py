from PIL import Image

im = Image.open(r'c:\Users\Gaby\Downloads\REPROGRAMACION ENERGETICA\logo.png')
bbox = im.getbbox()
if bbox:
    cropped = im.crop(bbox)
    cropped.save(r'c:\Users\Gaby\Downloads\REPROGRAMACION ENERGETICA\logo.png', "PNG")
    print("Trimmed logo bbox:", bbox, "New size:", cropped.size)
