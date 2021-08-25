import sys
import math



test_case = int(sys.stdin.readline())

for _ in range(test_case):
    m, n, x, y = map(int, sys.stdin.readline().split())

    # m, n 최소공배수
    lcm = (m * n) // math.gcd(m, n)

    while x <= lcm:
        if x%n == y%n:
            print(x)
            break
        x += m
    else:
        print(-1)

'''
def kaing(M, N, x, y): # 이 문제는 (1,1) -> (x,y)를 만드는 문제
    while x <= M*N: 
        if x % N == y % N: # 처음에는 x % N == y라고 생각했지만, 이러면 x % N은 0이 나오는데 y는 N인 경우 등이 생김
            return x # 답을 찾은 경우(만들어야 하는 x에서 M을 계속 더한 값이 횟수가 됨)
        x += M
    return -1 # 못 찾은 경우

T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())
    print(kaing(M, N, x, y))
'''