import re, urllib.request

u = ('https://readme-typing-svg.demolab.com/?lines=Directeur%20artistique%20junior'
     ";Design%20%26%20outils%20maison;Pyrotechnie%2C%20agents%20IA%2C%20self-hosted"
     ";Le%20design%20d'abord%2C%20le%20code%20ensuite"
     "&font=IBM%20Plex%20Mono&center=true&width=560&height=42&color=c07a45&vCenter=true&size=17&letterSpacing=1.5")
req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
svg = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
print('len', len(svg))
print('font-family:', sorted(set(re.findall(r"font-family=['\"]([^'\"]+)", svg)))[:4])
print('couleur:', sorted(set(re.findall(r'fill=["\']?(#[0-9a-fA-F]{6})', svg)))[:5])
print('lignes texte:', re.findall(r'<text[^>]*>([^<]{3,60})</text>', svg)[:6])
print('erreur?', 'not found' in svg.lower() or 'invalid' in svg.lower())
