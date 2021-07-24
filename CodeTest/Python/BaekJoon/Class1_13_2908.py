import sys

num1, num2 = map(int, sys.stdin.readline().split())
num1_changed, num2_changed = 0, 0

for i in range(2,-1,-1):
    num1_changed += (num1%10) * (10**i)
    num2_changed += (num2%10) * (10**i)

    num1 //= 10
    num2 //= 10

print(max(num1_changed, num2_changed))