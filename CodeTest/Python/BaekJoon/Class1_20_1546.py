import sys

n,*li = map(int, sys.stdin.read().split())
sum = 0

for i in range(n):
    sum += li[i]/max(li)*100

print(sum/n)