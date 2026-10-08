import urllib.request
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

# Check gallery pages
pages = [
    'https://dentalstudio.co/gallery/',
    'https://dentalstudio.co/implant-smile-gallery/',
    'https://dentalstudio.co/patient-gallery/',
    'https://dentalstudio.co/smile-makeover/',
]

for p in pages:
    print(f"\n=== FETCHING: {p} ===")
    content = fetch(p)
    if not content:
        continue
    
    # Find all images
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    print(f"Total images: {len(imgs)}")
    
    # Look for before/after patterns
    ba_pairs = []
    for img in imgs:
        if any(k in img.lower() for k in ['before', 'after', 'case', 'gallery', 'smile', 'patient', 'result']):
            print("  IMG:", img)
            
    # Also check if there are sections/cards with before and after
    snippets = re.findall(r'(.{0,100}(?:before|after|smile makeover|implant).{0,100})', content, re.IGNORECASE)
    print(f"Mentions of before/after: {len(snippets)}")
