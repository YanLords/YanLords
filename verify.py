import urllib.request, hashlib

local = open('/Users/yannicks/.hermes/cache/scratch/github_profile/README.md', 'rb').read()
print('local sha256 :', hashlib.sha256(local).hexdigest()[:16], len(local), 'bytes')

req = urllib.request.Request('https://raw.githubusercontent.com/YanLords/YanLords/main/README.md',
                             headers={'User-Agent': 'Mozilla/5.0'})
remote = urllib.request.urlopen(req, timeout=30).read()
print('remote sha256:', hashlib.sha256(remote).hexdigest()[:16], len(remote), 'bytes')
print('IDENTIQUE    :', local == remote)

req = urllib.request.Request('https://github.com/YanLords', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=40).read().decode('utf-8', 'replace')
print('\n--- page profil github.com/YanLords ---', len(html), 'bytes')
checks = {
    'titre "Ce que je construis" rendu': 'Ce que je construis' in html,
    'samp "Directeur artistique junior" rendu': 'Directeur artistique junior' in html,
    'bloc commente NON rendu (github-readme-stats absent)': 'github-readme-stats' not in html,
    'streak non rendu': 'streak-stats.demolab' not in html,
    'typing SVG rendu': 'readme-typing-svg' in html,
    'badge yandesign.fr rendu': 'yandesign.fr-f75c7e' in html,
    'GIF dev rendu': 'dev-working_rounded.gif' in html,
    'compteur visites rendu': 'visitor-badge' in html,
}
for k, v in checks.items():
    print(('OK   ' if v else 'ECHEC') + ' ' + k)
