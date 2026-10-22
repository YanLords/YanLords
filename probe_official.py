import urllib.request, re, time

def probe(u, label):
    for i in range(3):
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
            r = urllib.request.urlopen(req, timeout=30)
            t = r.read().decode('utf-8', 'replace')
            txts = [x.strip() for x in re.findall(r'<text[^>]*>(.*?)</text>', t) if x.strip()]
            err = 'Something went wrong' in t or 'Maximum retries' in t
            print(f'{label} try{i+1}: {len(t)}B err={err} texts={txts[:10]}')
            if not err and txts:
                return True
        except Exception as e:
            print(f'{label} try{i+1}: FAIL {type(e).__name__} {e}')
        time.sleep(4)
    return False

probe('https://github-readme-stats.vercel.app/api?username=YanLords&show_icons=true&theme=tokyonight', 'official-stats')
probe('https://streak-stats.demolab.com/?user=YanLords&theme=tokyonight&hide_border=true', 'streak-demolab')
probe('https://github-readme-streak-stats.herokuapp.com/?user=YanLords&theme=tokyonight&hide_border=true', 'streak-heroku')
