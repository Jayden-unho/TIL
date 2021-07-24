import sys

while(True):
    li = list(map(int, sys.stdin.readline().split()))

    if (sum(li) == 0):
        break

    li = sorted(li)

    if(li[0]**2 + li[1]**2 == li[2]**2): print("right")
    else: print("wrong")