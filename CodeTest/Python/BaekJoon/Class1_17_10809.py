import sys

str = sys.stdin.readline().rstrip()

for i in range(97,123):
    try:
        print(str.index(chr(i)), end=" ")
    except:
        print(-1, end=" ")


'''
import sys

s = sys.stdin.readline().rstrip()
alpha = {}

for i in range(97,123):
    alpha[chr(i)] = -1

for j in range(len(s)):
    if alpha[s[j]] == -1:
        alpha[s[j]] = j

for v in alpha.values():
    print(v, end=' ')
'''