import os
from PIL import Image

uploaded = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\1ba0dda2-b386-43ee-9743-286e608e1d0f\.user_uploaded'

# 1. Doctors image: media_1790056778550.png (1024 x 272)
# There are 3 doctor photos side by side with white space.
doc_img = Image.open(os.path.join(uploaded, 'media_1790056778550.png'))
w, h = doc_img.size

# Let's find the bounding box of non-white areas or slice horizontally into 3 photos
# In a 1024 width image, three photos are placed across the width:
# Left photo: approx x: 60 to 300, y: 30 to 260
# Middle photo: approx x: 380 to 620, y: 30 to 260
# Right photo: approx x: 700 to 940, y: 30 to 260

# Let's inspect non-white bounding boxes per column
import numpy as np
arr = np.array(doc_img.convert('RGB'))
# Threshold for white background: R>245, G>245, B>245
is_not_white = ~((arr[:, :, 0] > 240) & (arr[:, :, 1] > 240) & (arr[:, :, 2] > 240))
col_has_content = is_not_white.any(axis=0)

# Find segments of content columns
segments = []
in_seg = False
start = 0
for x, val in enumerate(col_has_content):
    if val and not in_seg:
        in_seg = True
        start = x
    elif not val and in_seg:
        in_seg = False
        if x - start > 50: # valid image segment
            segments.append((start, x))
if in_seg and (w - start > 50):
    segments.append((start, w))

print("Found doctor segments (x-range):", segments)

doctor_names = ['doctor-sudhir-yadav.jpg', 'doctor-archana-yadav.jpg', 'doctor-varun-dahiya.jpg']

for i, (x1, x2) in enumerate(segments):
    if i < 3:
        # find vertical bounding box in this segment
        seg_content = is_not_white[:, x1:x2]
        row_has_content = seg_content.any(axis=1)
        y_indices = np.where(row_has_content)[0]
        if len(y_indices) > 0:
            y1, y2 = y_indices[0], y_indices[-1]
            cropped = doc_img.crop((x1, y1, x2, y2))
            cropped.convert('RGB').save(doctor_names[i], quality=95)
            print(f"Saved {doctor_names[i]}: box ({x1}, {y1}, {x2}, {y2}), size: {cropped.size}")

# 2. Clinic image from media_1790056846281.png
# In media_1790056846281.png (1024 x 428):
# The left half is the clinic photo card!
clinic_screenshot = Image.open(os.path.join(uploaded, 'media_1790056846281.png'))
cw, ch = clinic_screenshot.size

c_arr = np.array(clinic_screenshot.convert('RGB'))
c_not_white = ~((c_arr[:, :, 0] > 245) & (c_arr[:, :, 1] > 245) & (c_arr[:, :, 2] > 245))

# The clinic card is on the left (x roughly 70 to 480, y roughly 60 to 370)
# Let's crop the left content card
c_left = c_not_white[:, :cw//2]
r_indices = np.where(c_left.any(axis=1))[0]
c_indices = np.where(c_left.any(axis=0))[0]
if len(r_indices) > 0 and len(c_indices) > 0:
    cy1, cy2 = r_indices[0], r_indices[-1]
    cx1, cx2 = c_indices[0], c_indices[-1]
    clinic_card = clinic_screenshot.crop((cx1, cy1, cx2, cy2))
    clinic_card.convert('RGB').save('clinic-about.jpg', quality=95)
    print(f"Saved clinic-about.jpg: box ({cx1}, {cy1}, {cx2}, {cy2}), size: {clinic_card.size}")

print("Asset extraction complete.")
