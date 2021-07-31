# 재귀함수를 이용한 피보나치 수 구하기
import sys


def fibo(num):
    # Base Case
    if num == 0:
        return num
    elif num == 1:
        return num
        
    return fibo(num-1) + fibo(num-2)


number = int(sys.stdin.readline())
print(fibo(number))