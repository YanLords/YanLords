import urllib.request, re
u = 'https://streak-stats.demolab.com/?user=YanLords&theme=tokyonight&hide_border=true'
r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30)
t = r.read().decode('utf-8', 'replace')
print(len(t))
print(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' | ', t))[:1500])
