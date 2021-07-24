import sys

num = int(sys.stdin.readline().rstrip())
i = 0

while num > 0:
    if i == 0:
        num -= 1
        i += 1
        continue

    num = num-(6*i)
    i += 1

print(i)