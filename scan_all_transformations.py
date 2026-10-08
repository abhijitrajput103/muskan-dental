import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
}

def exists(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status == 200
    except:
        return False

base = 'https://dentalstudio.co/public/dental-transformation/'

# Check categories
checks = {
    'veneers': [f'veneers{i}.jpg' for i in range(1, 16)],
    'smile_makeover': [f'smile-makeover-{i}.jpg' for i in range(1, 10)],
    'crowns_bridges': [f'cb{i}.png' for i in range(1, 8)] + [f'cb{i}.jpg' for i in range(1, 8)],
    'rct': [f'rct{i}.png' for i in range(1, 10)] + [f'rct{i}.webp' for i in range(1, 10)],
    'whitening': [f'whitening{i}.png' for i in range(1, 5)] + [f'whitening{i}.jpg' for i in range(1, 5)],
    'braces': [f'braces{i}.png' for i in range(1, 6)] + [f'braces{i}.jpg' for i in range(1, 6)],
    'aligners': [f'aligners{i}.png' for i in range(1, 6)] + [f'aligners{i}.jpg' for i in range(1, 6)],
    'fmr': [f'fmr{i}.jpg' for i in range(1, 18)] + [f'fmr{i}.jpeg' for i in range(1, 18)],
    'fm_implants': [f'fm-case{i}.jpg' for i in range(1, 10)] + [f'fm-case{i}.png' for i in range(1, 10)],
    'single_implant': [f'si-case{i}.png' for i in range(1, 10)] + [f'si-case{i}.jpg' for i in range(1, 10)],
    'multiple_implants': [f'mi-case{i}.png' for i in range(1, 10)] + [f'mi-case{i}.jpg' for i in range(1, 10)],
    'general_gallery': [f'{i}.jpg' for i in range(1, 18)],
}

found = {}
for cat, files in checks.items():
    found[cat] = []
    for f in files:
        url = base + f
        if exists(url):
            found[cat].append(url)
            print(f"[{cat}] Found {f}")

print("\n--- Summary ---")
for cat, urls in found.items():
    print(f"{cat}: {len(urls)} images")
