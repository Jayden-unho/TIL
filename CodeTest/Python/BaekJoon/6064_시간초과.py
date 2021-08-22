'''
m,n 두 수의 최소공배수가 최대
어떠한 수를 m,n 나눈 나머지가 x,y 인 수를 구하면 됨
'''

import sys
import math



test_case = int(sys.stdin.readline())

for _ in range(test_case):
    m, n, x, y = map(int, sys.stdin.readline().split())
    x_list = set()
    y_list = set()

    # m, n 최소공배수
    lcm = (m * n) // math.gcd(m, n)

    i = 0
    while x+(m*i) <= lcm or y+(n*i) <= lcm:
        x_list.add(x + (m*i))
        y_list.add(y + (n*i))
        i += 1

    answer = x_list.intersection(y_list)

    if not answer:
        answer = -1
    else:
        answer = answer.pop()
    
    print(answer)