'''
m,n 두 수의 최소공배수가 최대
어떠한 수를 m,n 나눈 나머지가 x,y 인 수를 구하면 됨
시간초과
'''

import sys
import math



test_case = int(sys.stdin.readline())

for _ in range(test_case):
    m, n, x, y = map(int, sys.stdin.readline().split())

    # m, n 최소공배수
    lcm = (m * n) // math.gcd(m, n)

    answer = [0] * (lcm + 1)

    tmp_x = tmp_y = 0
    idx = 0
    # 이 부분이 문제 같음... 반복을 줄일  방법 필요
    while tmp_x <= lcm or tmp_y <= lcm:
        tmp_x = x + (m * idx)
        tmp_y = y + (n * idx)

        if tmp_x <= lcm:
            answer[tmp_x] += 1
        if tmp_y <= lcm:
            answer[tmp_y] += 1

        idx += 1
    
    if not answer.count(2):
        print(-1)
    else:
        print(answer.index(2))
