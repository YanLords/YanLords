import urllib.request, re

def fetch(u):
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    r = urllib.request.urlopen(req, timeout=40)
    return r.status, r.headers.get('content-type'), r.read()

st, ct, html_b = fetch('https://github.com/YanLords')
html = html_b.decode('utf-8', 'replace')
print('profil', st, len(html), 'bytes')

checks = {
    'banner relatif present': 'assets/banner.svg' in html,
    'ancien GIF retire': 'dev-working_rounded.gif' not in html,
    'Planete Pyro Dist. rendu (samp)': 'Planete Pyro Dist. &#64;' in html or 'Planete Pyro Dist.' in html,
    'Plus de "Planète Artifice"': 'Planète Artifice' not in html,
    'typing svg': 'readme-typing-svg' in html,
    'stats toujours cachees': 'github-readme-stats' not in html,
}
for k, v in checks.items():
    print(('OK   ' if v else 'ECHEC') + ' ' + k)

m = re.search(r'https://camo\.githubusercontent\.com/[^"\s]+', html)
print('\nimage camo trouvee:', bool(m), (m.group(0)[:90] + '...') if m else '')

for u in ['https://github.com/YanLords/YanLords/raw/main/assets/banner.svg',
          'https://raw.githubusercontent.com/YanLords/YanLords/main/assets/banner.svg']:
    try:
        st, ct, b = fetch(u)
        print(f'{st} {ct} {len(b)}B  {u}')
    except Exception as e:
        print('FAIL', u, type(e).__name__, e)
