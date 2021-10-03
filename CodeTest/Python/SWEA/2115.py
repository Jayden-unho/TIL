import sys
from pprint import pprint
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    hive = [list(map(int, input().split())) for _ in range(N)]
    price = [[0] * N for _ in range(N)]
    coordinate = (0, 0)
    answer = 0
    

    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                if sum(hive[i][j:j+M]) <= C:                    # 합이 기준을 안넘으면
                    price[i][j] += (hive[i][j+k] ** 2)          # 가격 누적합 쌓기
                else:                                           # 합이 기준을 넘으면
                    tmp_sum = 1
                    for num in hive[i][j:j+M]:
                        tmp_sum |= (tmp_sum << (num**2))
                
                    print(bin(tmp_sum))
                    for num in range(C**2, -1, -1):
                        if tmp_sum & (1 << num):
                            price[i][j] = num
                            break
                    

            if price[i][j] >= answer:
                coordinate = (i, j)
                answer = price[i][j]
                
    for i in range(-M+1, M, 1):
        price[coordinate[0]][coordinate[1] + i] = 0

    second = 0
    for i in range(N):
        tmp = max(price[i])
        if tmp >= second:
            second = tmp
    
    answer += second
    print('#{} {}'.format(tc, answer))