import re, pathlib
src = pathlib.Path('yd_Logo_Blanc.svg').read_text(encoding='utf-8')
ink = src.replace('#FAFAF9', '#0D100F').replace('fill="white"', 'fill="#0D100F"')
pathlib.Path('yd_Logo_Ink.svg').write_text(ink, encoding='utf-8')
print('fills ink:', sorted(set(re.findall(r'fill="([^"]+)"', ink))))
print('ok yd_Logo_Ink.svg', len(ink), 'bytes')
