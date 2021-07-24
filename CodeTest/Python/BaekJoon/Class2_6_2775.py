#백준 숏코딩
import math

i = lambda:int(input())
exec('k,n=i(),i();print(math.comb(k+n,k+1));'*i())

'''
#백준 숏코딩 #2
import math

for _ in range(int(input())):
  k = int(input())
  n = int(input())
  print(math.comb(n+k,n-1))
'''


'''
#내가 짠 코드
import sys

testCase = int(sys.stdin.readline().rstrip())

for _ in range(testCase):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    li = [1 for _ in range(n+1)]

    for i in range(k+1):
        for j in range(2, n+1):
            li[j] = li[j] + li[j-1]
    
    print(li[-1])
'''