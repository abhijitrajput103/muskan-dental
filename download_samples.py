import urllib.request
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

os.makedirs('sample_downloads', exist_ok=True)

test_urls = [
    'https://dentalstudio.co/public/dental-transformation/veneers1.jpg',
    'https://dentalstudio.co/public/dental-transformation/smile-makeover-1.jpg',
    'https://dentalstudio.co/public/dental-transformation/rct1.png',
    'https://dentalstudio.co/public/dental-transformation/fm-case1.jpg',
    'https://dentalstudio.co/public/dental-transformation/whitening1.png',
    'https://dentalstudio.co/public/dental-transformation/aligners1.png',
]

for u in test_urls:
    fname = os.path.basename(u)
    dest = os.path.join('sample_downloads', fname)
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            with open(dest, 'wb') as f:
                f.write(data)
            print(f"Downloaded {fname}: {len(data)} bytes")
    except Exception as e:
        print(f"Failed {u}: {e}")
