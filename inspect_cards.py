import urllib.request, re

def get(u):
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Accept': '*/*'})
    r = urllib.request.urlopen(req, timeout=25)
    return r.status, r.headers.get('content-type'), r.read()

# 1) stats card: is it a real card or an error card?
u = 'https://github-readme-stats.vercel.app/api?username=YanLords&show_icons=true&theme=tokyonight&include_all_commits=true&count_private=true'
st, ct, d = get(u)
t = d.decode('utf-8', 'replace')
print('STATS CARD', st, ct, len(d))
print('  texts:', re.findall(r'<text[^>]*>(.*?)</text>', t)[:20])
print('  error-ish:', [w for w in ('Something went wrong', 'error', 'Could not') if w.lower() in t.lower()])

ul = 'https://github-readme-stats.vercel.app/api/top-langs/?username=YanLords&show_icons=true&theme=tokyonight&layout=compact&langs_count=8'
st, ct, d = get(ul)
t = d.decode('utf-8', 'replace')
print('LANGS CARD', st, ct, len(d))
print('  texts:', re.findall(r'<text[^>]*>(.*?)</text>', t)[:20])

# 2) Hi.gif: blob vs raw
for u in ['https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Hi.gif',
          'https://raw.githubusercontent.com/TheDudeThatCode/TheDudeThatCode/master/Assets/Hi.gif']:
    st, ct, d = get(u)
    print('HIGIF', st, ct, len(d), u)
