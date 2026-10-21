#!/usr/bin/env python3
"""Re-embed smoke.png into index.html's base64 fallback.
Usage: python3 embed_smoke.py   (run in the folder with index.html and smoke.png)"""
import base64, re, os
d = os.path.dirname(os.path.abspath(__file__))
html = os.path.join(d, 'index.html')
b64 = base64.b64encode(open(os.path.join(d, 'smoke.png'), 'rb').read()).decode()
s = open(html, encoding='utf-8').read()
s, n = re.subn(r'const SMOKE_B64="data:image/png;base64,[A-Za-z0-9+/=]*";',
               'const SMOKE_B64="data:image/png;base64,' + b64 + '";', s)
if n != 1: raise SystemExit('SMOKE_B64 line not found in index.html')
open(html, 'w', encoding='utf-8').write(s)
print('Embedded smoke.png (%d bytes) into index.html' % len(base64.b64decode(b64)))
