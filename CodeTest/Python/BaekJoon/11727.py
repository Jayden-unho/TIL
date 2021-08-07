import sys


num = int(sys.stdin.readline())
answer=[0, 1]

for n in range(2, num+1):
    if n%2:
        answer.append((answer[n-1]*2 - 1) % 10007)
    else:
        answer.append((answer[n-1]*2 + 1) % 10007)

print(answer[num])