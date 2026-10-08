import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error {url}: {e}")
        return ""

# Inspect gallery and implant-smile-gallery
for page in ['https://dentalstudio.co/implant-smile-gallery/', 'https://dentalstudio.co/gallery/']:
    print(f"\n--- {page} ---")
    c = fetch(page)
    # print all images or data-src or background-image
    all_imgs = re.findall(r'(?:src|data-src|href)=["\']([^"\']+\.(?:jpg|jpeg|png|webp))["\']', c, re.IGNORECASE)
    print("Found images:", len(all_imgs))
    for img in sorted(set(all_imgs)):
        print(" ", img)
