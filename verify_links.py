import os
import re

base = os.path.dirname(os.path.abspath(__file__))
html_files = [f for f in os.listdir(base) if f.endswith('.html')]

missing = []

for hf in html_files:
    path = os.path.join(base, hf)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # <base> (used by 404.html) points at the site root, not at a file
    content = re.sub(r'<base\b[^>]*>', '', content)

    srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)

    for s in srcs:
        if s.startswith(('http', '#', 'data:', 'javascript:')):
            continue
        clean_s = s.split('?')[0]
        full_p = os.path.normpath(os.path.join(base, clean_s))
        if not os.path.exists(full_p):
            missing.append((hf, 'src', s))

    for h in hrefs:
        if h.startswith(('http', '#', 'mailto:', 'javascript:', 'tel:')):
            continue
        clean_h = h.split('#')[0]
        if not clean_h:
            continue
        full_p = os.path.normpath(os.path.join(base, clean_h))
        if not os.path.exists(full_p):
            missing.append((hf, 'href', h))

if missing:
    print("MISSING REFERENCES FOUND:")
    for m in missing:
        print(f"File: {m[0]} | Attribute: {m[1]} | Target: {m[2]}")
else:
    print("SUCCESS: ALL ASSET AND LINK REFERENCES EXIST AND ARE 100% VALID!")
