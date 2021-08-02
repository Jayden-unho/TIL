import math

def solution(n):
    prime_number = [True for _ in range(n+1)]
    prime_number[0] = prime_number[1] = False

    for num in range(2, int(math.sqrt(n+1)+1)):
        mul = 2
        while num*mul <= n:
            prime_number[num*mul] = False
            mul += 1  

    return prime_number.count(True)

print(solution(10))
print(solution(5))