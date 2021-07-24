testCase = int(input())

for i in range(1, testCase+1):
    boardSize, flySwatterSize = map(int, input().split())
    max_deadFly = 0

    # 배열에 파리의 갯수를 2차원 배열로 설정
    board = [list(map(int, input().split())) for _ in range(boardSize)]
    
    for a in range(boardSize - flySwatterSize + 1):
        for x in range(boardSize - flySwatterSize + 1):
            deadFly = 0
            for b in range(a, a+flySwatterSize):
                for y in range(x, x+flySwatterSize):
                    deadFly += board[b][y]
            
            if max_deadFly < deadFly:
                max_deadFly = deadFly

    print(f'#{i} {max_deadFly}')