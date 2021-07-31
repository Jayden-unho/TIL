import sys

testCase = int(sys.stdin.readline().rstrip())

for _ in range(testCase):
    h,w,n = map(int, sys.stdin.readline().split())

    if(n%h != 0):  
        print((n%h)*100 + n//h + 1)
    else:
        print(h*100 + n//h)