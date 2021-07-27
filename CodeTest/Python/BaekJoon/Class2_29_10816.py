import sys

# num1 : 숫자 카드의 갯수 / num1_list : 숫자 카드의 숫자들
num1 = int(sys.stdin.readline())
num1_list = list(map(int, sys.stdin.readline().split()))
num1_dict = {}

# 딕셔너리에 각 숫자들 나온 횟수 입력
for n in num1_list:
    num1_dict[n] = num1_dict.get(n, 0) + 1

# num2 : 비교할 숫자들 갯수 / num2_list : 비교할 숫자 리스트
num2 = int(sys.stdin.readline())
num2_list = list(map(int, sys.stdin.readline().split()))

# 출력
for n in num2_list:
    print(num1_dict.get(n, 0))