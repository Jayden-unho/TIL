import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(N)])
answer = 0

plus = []
minus = []

for num in nums:
    if num > 0:
        plus.append(num)
    else:
        minus.append(num)

minus = minus[::-1]

while True:
    if len(plus) <= 1 and len(minus) <= 1:
        answer += sum(plus + minus)
        break

    if len(plus) > 1:
        n1 = plus.pop()
        n2 = plus.pop()

        if n2 > 1:
            answer += n1 * n2
        else:
            answer += n1 + n2

    if len(minus) > 1:
        n1 = minus.pop()
        n2 = minus.pop()

        answer += n1 * n2

print(answer)
