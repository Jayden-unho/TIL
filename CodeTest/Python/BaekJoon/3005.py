import sys
sys.stdin = open('input.txt')

R, C = map(int, sys.stdin.readline().split())

tables = [sys.stdin.readline().rstrip() for _ in range(R)]

words = set()
for r in range(R):
    row = tables[r].split('#')

    for word in row:
        if (len(word) >= 2):
            words.add(word)

for c in range(C):
    col = ''.join([tables[r][c] for r in range(R)]).split('#')

    for word in col:
        if (len(word) >= 2):
            words.add(word)

answer = sorted(words)[0]
print(answer)
