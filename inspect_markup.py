import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode('utf-8', errors='ignore')

html = fetch('https://dentalstudio.co/dental-veneers/')

# Find the section containing dental-transformation
pattern = re.compile(r'<section[^>]*class=["\'][^"\']*(?:transformation|case|gallery|before)[^"\']*["\'][^>]*>.*?</section>', re.DOTALL | re.IGNORECASE)
matches = pattern.findall(html)
if not matches:
    # Look for any container with veneers1.jpg
    idx = html.find('veneers1.jpg')
    if idx != -1:
        start = max(0, idx - 500)
        end = min(len(html), idx + 1000)
        print("Context around veneers1.jpg:")
        print(html[start:end])
else:
    for m in matches:
        print("Matched section:")
        print(m[:1000])
