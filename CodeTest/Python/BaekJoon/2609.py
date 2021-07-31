import sys

num1, num2 = map(int, sys.stdin.readline().split())

gcd = 1 # Greatest Common Denominator, 최대공약수
lcm = 1 # Least(Lowest) Common Multiple, 최소공배수

# num1을 큰수로 지정하기 위함
if num1 < num2:
    num1, num2 = num2, num1

# 최대공약수
if num1 == num2:
    gcd = num1
elif num1%num2 == 0:
    gcd = num2
else:
    for i in range(num2//2, 0, -1):
        if num1%i == 0 and num2%i == 0:
            gcd = i
            break

# 최소공배수
lcm = num1*num2//gcd

print(f'{gcd}\n{lcm}')