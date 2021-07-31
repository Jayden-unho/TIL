import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1,n+1):
    sum = i
    k = i
    while k > 0:
        sum += k%10
        k //= 10
    
    if sum == n:
        print(i)
        break

    if i == n:
        print(0)