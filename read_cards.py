import urllib.request, re

def texts(u):
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    t = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
    return [x.strip() for x in re.findall(r'<text[^>]*>(.*?)</text>', t) if x.strip()]

base = 'https://github-readme-stats-eight-theta.vercel.app/api'
print('STATS :', texts(f'{base}?username=YanLords&show_icons=true&theme=tokyonight&include_all_commits=true&count_private=true'))
print()
print('LANGS :', texts(f'{base}/top-langs/?username=YanLords&show_icons=true&theme=tokyonight&layout=compact&langs_count=8'))
print()
st = texts('https://github-readme-streak-stats.herokuapp.com/?user=YanLords&theme=tokyonight&hide_border=true')
print('STREAK:', st)
