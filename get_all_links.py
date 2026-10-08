import re

with open('dentalstudio_home.html', 'r', encoding='utf-8') as f:
    html = f.read()

links = set(re.findall(r'href=["\'](https://dentalstudio\.co/[^"\'#\s]*)["\']', html))
print(f"Total internal links on homepage: {len(links)}")
for l in sorted(links):
    print(" ", l)
