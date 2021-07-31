# 재귀함수를 이용하여 팩토리얼 구현
import sys


def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)


number = int(sys.stdin.readline())
print(factorial(number))