import sys

a,b,c = map(int, sys.stdin.read().split())
li = [0]*10
result = a*b*c

while result != 0:
    li[result%10] += 1
    result = result//10

for i in range(10):
    print(li[i])