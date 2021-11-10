import sys
sys.stdin = open('input.txt')


N = int(sys.stdin.readline())
answer = 0
prime_num = [False, False] + [True] * (N-1)
prime_num_li = []

for i in range(2, int(N**0.5)+1):
    if prime_num[i]:
        j = 2
        while i * j < len(prime_num):
            prime_num[i*j] = False
            j += 1

for i in range(len(prime_num)):
    if prime_num[i]:
        prime_num_li.append(i)

l = r = 0
while l < len(prime_num_li):
    tmp_sum = 0
    while tmp_sum < N and r < len(prime_num_li):
        tmp_sum += prime_num_li[r]
        if tmp_sum == N:
            answer += 1
            break
        r += 1

    l += 1
    r = l

print(answer)