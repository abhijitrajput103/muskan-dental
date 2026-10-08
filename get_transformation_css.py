import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}
req = urllib.request.Request('https://dentalstudio.co/public/css/pages/treatment.css', headers=headers)
content = urllib.request.urlopen(req).read().decode('utf-8')

start = content.find('Dental Transformation Gallery Styles')
if start != -1:
    print(content[start:start+1800])
