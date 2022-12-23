import sys
sys.stdin = open('input.txt')

table = {}

for _ in range(int(sys.stdin.readline())):
    s, t = map(int, sys.stdin.readline().split())
    table[s] = table.get(s, 0) + 1
    table[t] = table.get(t, 0) - 1

answer = 0
room = 0
for key in sorted(table.keys()):
    room += table[key]
    if answer < room:
        answer = room

print(answer)
