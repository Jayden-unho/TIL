testCase = int(input())
 
for i in range(1, testCase+1):
    boardSize, wordLength = map(int, input().split())
     
    # 보드 만들기
    board = [list(map(int, input().split())) for _ in range(boardSize)]
    # 정답 담아두는 리스트
    answer = []
     
    # 가로 체크 - 2중 for [x][y]
    # 세로 체크 - 2중 for [y][x]
    for x in range(boardSize):
        width_len = 0
        height_len = 0
         
        for y in range(boardSize):
            # 가로
            if board[x][y] == 0: 
                if width_len != 0: # 길이가 0이 아니면
                    answer.append(width_len) # 길이가 0이 아니면, 값을 담는다
                    width_len = 0
            elif y == 0 or board[x][y-1] == 0: width_len = 1 # y가 0 이거나 [x][y-1]의 값이 0이면
            else: width_len += 1 # 이전에 1이고 지금도 1일때 길이 증가
                 
                 
            # 세로
            if board[y][x] == 0: 
                if height_len != 0:
                    answer.append(height_len)
                    height_len = 0
            elif y == 0 or board[y-1][x] == 0: height_len = 1
            else: height_len += 1
                 
            if y == boardSize-1:# 마지막 인덱스인 경우
                answer.append(width_len)
                answer.append(height_len)
         
    print(f'#{i} {answer.count(wordLength)}')