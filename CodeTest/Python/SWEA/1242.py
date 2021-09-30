import sys
from pprint import pprint
sys.stdin = open('input.txt')


CODE_DICT = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9,
}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    bin_code = set()

    for _ in range(N):
        temp = int(input(), 16)
        
        if temp:
            temp = bin(temp).rstrip('0')
            # print(f'LOG --- TEMP : {temp}')
            
            for i in range(1, 10):
                end = len(temp)
                start = len(temp) - (i*7)
                element = temp[start:end]
                
                cnt = [0] * 4
                idx = 0
                v = 0

                for e in element:
                    if int(e) == v:
                        cnt[idx] += 1
                    else:
                        idx += 1
                        if not v:
                            v = 1
                        elif v == 1:
                            v = 0
                        cnt[idx] += 1
                
                if CODE_DICT.get(tuple(cnt)):
                    break
            
    print(temp)