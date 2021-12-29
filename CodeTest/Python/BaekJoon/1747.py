import sys


N = int(sys.stdin.readline())               # 특정 숫자
prime_num = [1] * 1003002                   # 정답이 나올 수 있는 최대 숫자까지만 리스트 생성
prime_num[0] = prime_num[1] = 0             # 0, 1은 소수가 아니므로

for i in range(2, int(1003002**0.5) + 1):   # 에라토스테네스의 체
    if prime_num[i]:
        mul = 2
        while mul * i < 1003002:
            prime_num[i*mul] = 0
            mul += 1

idx = 0                                     # 특정 보다 얼마나 큰지 결정할 변수
while True:
    reverse_num = 0                         # 앞뒤가 바뀐 숫자를 저장할 변수
    num = N + idx                           # 특정 수보다 idx 크기만큼 큰 수

    if prime_num[num]:                      # 지금 숫자가 소수라면
        while num:                          # 숫자를 거꾸로 만들어서 저장
            reverse_num = (reverse_num * 10) + (num % 10)
            num //= 10

        if reverse_num == N + idx:          # 숫자를 거꾸로 해도 같다면
            print(reverse_num)              # 출력 및 종료
            break

    idx += 1