import os

files = [f for f in os.listdir('.') if f.endswith('.jpg')]
with open('test_view.html', 'w') as f:
    f.write('<!DOCTYPE html><html><head><style>body{font-family:sans-serif;display:flex;flex-wrap:wrap;gap:20px;} .card{border:1px solid #ccc;padding:10px;width:320px;} img{width:100%;height:auto;}</style></head><body>\n')
    for img in files:
        f.write(f'<div class="card"><h4>{img}</h4><img src="{img}"></div>\n')
    f.write('</body></html>')
print("Generated test_view.html")
