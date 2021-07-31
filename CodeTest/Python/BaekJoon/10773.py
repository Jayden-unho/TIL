import sys

number = int(sys.stdin.readline())
answer = []

for _ in range(number):
    num = int(sys.stdin.readline())

    if num == 0:
        answer.pop()
    else:
        answer.append(num)

print(sum(answer))