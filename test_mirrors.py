import urllib.request, re, time

Q = 'username=YanLords&show_icons=true&theme=tokyonight&include_all_commits=true&count_private=true'
hosts = [
    'https://github-readme-stats.vercel.app/api',
    'https://github-readme-stats-eight-theta.vercel.app/api',
    'https://github-readme-stats-sigma-five.vercel.app/api',
    'https://github-readme-stats-git-masterorgs-github-readme-stats-team.vercel.app/api',
]
for h in hosts:
    u = f'{h}?{Q}'
    for attempt in range(2):
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
            r = urllib.request.urlopen(req, timeout=30)
            t = r.read().decode('utf-8', 'replace')
            err = 'Something went wrong' in t
            print(f'{"ERR " if err else "OK  "} {len(t):6}B {h}  texts={re.findall(chr(60)+"text[^>]*>(.*?)<", t)[:6] if not err else t[:120]}')
            if not err:
                break
        except Exception as e:
            print('FAIL', h, type(e).__name__, e)
        time.sleep(2)
