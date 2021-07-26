import sys

num = int(sys.stdin.readline())
primeNumber = []

num_list = list(map(int, sys.stdin.readline().split()))

for n in num_list:
    sign = True
    for i in range(2, n):
        if n%i == 0:
            sign = False
            break
    if sign == True and n != 1:
        primeNumber.append(n)

print(len(primeNumber))