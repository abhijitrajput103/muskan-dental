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
        return ""

treatment_urls = [
    'https://dentalstudio.co/dental-implant/',
    'https://dentalstudio.co/dental-veneers/',
    'https://dentalstudio.co/crowns-and-bridges/',
    'https://dentalstudio.co/smile-makeover/',
    'https://dentalstudio.co/root-canal/',
    'https://dentalstudio.co/teeth-whitening/',
    'https://dentalstudio.co/braces-treatment/',
    'https://dentalstudio.co/aligners/',
    'https://dentalstudio.co/full-mouth-rehabilitation/',
    'https://dentalstudio.co/full-mouth-dental-implants/',
    'https://dentalstudio.co/single-tooth-implant/',
    'https://dentalstudio.co/multiple-teeth-implants/',
    'https://dentalstudio.co/implant-smile-gallery/',
    'https://dentalstudio.co/patient-gallery/',
    'https://dentalstudio.co/testimonials/',
]

results = {}

for u in treatment_urls:
    c = fetch(u)
    if not c:
        continue
    # find images in before/after or transformations
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', c)
    # also background images or data-src
    bg_imgs = re.findall(r'url\(["\']?([^"\'\)]+\.(?:jpg|jpeg|png|webp))["\']?\)', c)
    data_imgs = re.findall(r'data-src=["\']([^"\']+)["\']', c)
    all_imgs = set(imgs + bg_imgs + data_imgs)
    
    # filter for interesting images (dental transformations, cases, before/after)
    interesting = [img for img in all_imgs if any(k in img.lower() for k in [
        'transform', 'before', 'after', 'case', 'smile', 'patient', 'result', 'implant', 'veneer', 'crown', 'rct'
    ]) and not any(k in img.lower() for k in ['logo', 'icon', 'favicon', 'cost-mumbai', 'quality-precise'])]
    
    if interesting:
        results[u] = interesting
        print(f"\n=== {u} ({len(interesting)} imgs) ===")
        for img in interesting:
            print(" ", img)
    else:
        print(f"\n=== {u}: No before/after images found ===")
