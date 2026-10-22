import re, urllib.request

txt = open('README.md').read()
urls = set()
for m in re.finditer(r'\((https?://[^\)\s]+)\)', txt):
    urls.add(m.group(1))
for m in re.finditer(r'src="(https?://[^"]+)"', txt):
    urls.add(m.group(1))
for m in re.finditer(r'srcset="([^"]+)"', txt):
    urls.add(m.group(1))

bad = []
for u in sorted(urls):
    uu = u.replace(' ', '%20').replace('&amp;', '&')
    try:
        req = urllib.request.Request(uu, headers={'User-Agent': 'Mozilla/5.0', 'Accept': '*/*'})
        r = urllib.request.urlopen(req, timeout=30)
        body = r.read()
        ct = r.headers.get('content-type', '')
        txtbody = body.decode('utf-8', 'replace') if 'svg' in ct or 'html' in ct else ''
        err = any(k in txtbody for k in ('Something went wrong', 'not found', 'Invalid', 'error'))
        ok = r.status == 200 and len(body) > 100 and not err
        if not ok:
            bad.append((uu, r.status, len(body), err))
        print(('OK   ' if ok else 'SUSP ') + f'{r.status} {len(body):>7}B {ct[:22]:22} {uu[:88]}')
    except Exception as e:
        bad.append((uu, type(e).__name__, str(e), ''))
        print(f'FAIL {type(e).__name__}: {e} -- {uu[:88]}')

print('\nTOTAL', len(urls), '| problemes:', len(bad))
for b in bad:
    print('  ->', b)
