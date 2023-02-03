import sys
import re
sys.stdin = open('input.txt')

html = sys.stdin.readline().rstrip()
html = re.sub('</?(main)?(div)?>', '', html)
html = re.split('</?p>', html)

for s in html:
    if not s:
        continue

    if s.startswith('<div'):
        title = re.search('(?<=title=\")[a-zA-Z0-9\_\s]*', s).group(0)
        print(f'title : {title.strip()}')
    else:
        s = re.sub('</?[^<>]*>', '', s)
        s = re.sub('\s+', ' ', s)
        print(s.strip())
