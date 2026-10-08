import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode('utf-8', errors='ignore')

# Check how dental-transformation-gallery is styled
html = fetch('https://dentalstudio.co/dental-veneers/')
css_links = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', html)
print("CSS links:", css_links)

for css_url in css_links:
    css_content = fetch(css_url)
    if 'transformation' in css_content.lower() or 'gallery-card' in css_content.lower():
        print(f"\nFound in {css_url}:")
        for line in css_content.splitlines():
            if any(k in line.lower() for k in ['gallery-grid', 'gallery-card', 'transformation']):
                print(" ", line[:120])
