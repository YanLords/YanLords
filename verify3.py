import urllib.request, re

def fetch(u):
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    r = urllib.request.urlopen(req, timeout=40)
    return r.status, r.headers.get('content-type'), r.read()

st, ct, html_b = fetch('https://github.com/YanLords')
html = html_b.decode('utf-8', 'replace')
print('profil', st, len(html), 'bytes')
checks = {
    'banner.png reference': 'assets/banner.png' in html,
    'ancien banner.svg absent': 'assets/banner.svg' not in html,
    'ancien GIF absent': 'dev-working_rounded.gif' not in html,
    'Planete Pyro Dist. present': 'Planete Pyro Dist.' in html,
    'stats cachees': 'github-readme-stats' not in html,
}
for k, v in checks.items():
    print(('OK   ' if v else 'ECHEC') + ' ' + k)

for u in ['https://github.com/YanLords/YanLords/raw/main/assets/banner.png',
          'https://raw.githubusercontent.com/YanLords/YanLords/main/assets/banner.png']:
    st, ct, b = fetch(u)
    print(f'{st} {ct} {len(b)}B  {u}')

# le premier camo de la page = le banner ?
m = re.search(r'https://camo\.githubusercontent\.com/[^"\s]+', html)
print('camo:', (m.group(0)[:80] + '...') if m else 'aucun')
