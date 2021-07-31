import sys



start_num, end_num = map(int, sys.stdin.readline().split())

# 종료하는 숫자까지 모두 소수라고 가정, 숫자 0은 인덱스 0으로 일치시킴
prime_num_list = [True for n in range(end_num+1)]
prime_num_list[0] = prime_num_list[1] = False

# 제곱근이 핵심
for idx in range(2, (end_num**0.5)+1):
    mul = 2
    
    # 숫자가 소수이면, 배수들 모두 소수가 아님
    if prime_num_list[idx]:
        while idx*mul <= end_num:
            prime_num_list[idx * mul] = False   # 소수의 배수들은 모두 False로 바꿈
            mul += 1

for idx in range(start_num, end_num+1):
    if prime_num_list[idx]:
        print(idx)