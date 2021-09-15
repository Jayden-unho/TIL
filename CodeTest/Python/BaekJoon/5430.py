""" 
Memory - 39704 KB (39.70 MB)
Time - 452 ms

주요 내용
- 데이터 입력과 출력 부분 주의
- 리스트를 R 명령이 있을때 마다 reverse() 를 한다면 시간 복잡도 증가
"""


import sys
from collections import deque


T = int(sys.stdin.readline())

for _ in range(T):
    P = sys.stdin.readline().strip()
    N = int(sys.stdin.readline())
    arr = deque([])
    if N:
        arr.extend(list(map(int, sys.stdin.readline().lstrip('[').rstrip(']\n').split(','))))
    else:
        bin = sys.stdin.readline()

    sign = -1    # -1 front / 1 back

    str_len = len(P)
    idx = 0
    while idx < str_len:
        if P[idx] == 'R':
            sign *= -1
        elif not arr:
            print('error')
            break
        elif sign == -1:
            arr.popleft()
        elif sign == 1:
            arr.pop()
        
        idx += 1

    else:
        if sign == 1:
            arr.reverse()

        print(f'[{",".join(list(map(lambda x: str(x), arr)))}]')