import sys


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
in_str = sys.stdin.readline().strip()

pn = ('IO'*n) + 'I'
pn_len = len(pn)
cnt = 0

sign = False
idx = 0
while idx <= (m - pn_len):
    if not sign and pn == in_str[idx : idx+pn_len]:
        idx += pn_len
        sign = True
        cnt += 1
    elif sign and in_str[idx : idx+2] == 'OI':
        idx += 2
        cnt += 1
    elif sign:
        sign = False
    else:
        sign = False
        idx += 1

print(cnt)