import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

period = 15 * 10 ** 5               # 나누는 수가 10^k 일때, 나머지는 주기를 이루는데 주기는 항상 15 * 10^(k-1) 이다.
fibo = [0, 1]                       # 피보나치 수열

for i in range(2, period):                              # 피보나치 수열을 주기의 길이만큼만 구함
    fibo.append((fibo[i-2] + fibo[i-1]) % 1000000)      # 피보나치 수열 값을 1,000,000 나눈 나머지의 값을 저장

print(fibo[N%period])               # 주기의 몇번쨰에 해당하는지 구해서 값 반환