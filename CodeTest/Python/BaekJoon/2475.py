import sys

#제곱을 구하는 함수
def Square(n):
    n = int(n)
    return n**2

#값들을 분리해서 Square 함수에 넣음
li = list(map(Square, sys.stdin.readline().split()))

#sum(list) - 리스트 합계 구하기
print(sum(li)%10)


'''
import sys

num = list(map(int, sys.stdin.readline().split()))
sum = 0

for a in num:
    sum += a**2

print(sum%10)
'''