import os
import glob
from PIL import Image

folder = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\1ba0dda2-b386-43ee-9743-286e608e1d0f\.tempmediaStorage"
files = glob.glob(os.path.join(folder, "*.*"))
files.sort(key=os.path.getmtime, reverse=True)

print("Recent files in .tempmediaStorage:")
for f in files[:10]:
    try:
        im = Image.open(f)
        print(os.path.basename(f), im.size, im.format, os.path.getmtime(f))
    except Exception as e:
        print(os.path.basename(f), os.path.getsize(f), e)
