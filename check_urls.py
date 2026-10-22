import re, urllib.request

txt = open('README.md').read()
urls = set()
for m in re.finditer(r'\((https?://[^\)]+)\)', txt):
    urls.add(m.group(1))
for m in re.finditer(r'src="(https?://[^"]+)"', txt):
    urls.add(m.group(1))
urls = {u for u in urls if any(k in u for k in ('img.shields', 'github-readme', 'readme-typing', 'visitor-badge', 'github.com/SP-XD', 'TheDudeThatCode'))}

bad = []
for u in sorted(urls):
    req = urllib.request.Request(u.replace(' ', '%20'), headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'image/*'})
    try:
        r = urllib.request.urlopen(req, timeout=25)
        st, ct, data = r.status, r.headers.get('content-type'), r.read()
        ok = st == 200 and len(data) > 200
        if not ok:
            bad.append(u)
        print(('OK  ' if ok else 'SUSP') + f' {st} {ct} {len(data)}B {u[:100]}')
    except Exception as e:
        bad.append(u)
        print(f'FAIL {type(e).__name__}: {e} -- {u[:100]}')

print('\nTOTAL', len(urls), '| problemes:', len(bad))
for b in bad:
    print('  ->', b)
