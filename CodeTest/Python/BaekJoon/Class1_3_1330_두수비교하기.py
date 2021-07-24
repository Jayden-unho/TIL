import sys

a,b = map(int, sys.stdin.readline().split())

#파이썬 삼항연산자 (if-else 한줄로 표현하기)
print(">" if a>b else ("<" if a<b else "=="))