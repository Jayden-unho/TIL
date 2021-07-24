testCase = int(input())

# row, column 의 인덱스값을 구하는데 사용됨
# 달팽이의 진행방향이 우->하->좌->상
# ex) 진행방향이 오른쪽이면 row 값은 변동이 없어야하고 column 값은 1씩 증가해야함
# 다음으로 아래로 진행시 row 값은 1씩 증가, column 값은 변동이 없어야 함
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for index in range(1, testCase+1):
    number = int(input())

    # number x number 크기의 2차원 배열 생성, 초기 값은 모두 0으로 시작
    board = [[0]*number for _ in range(number)]
    
    # 초기 row 와 column 은 0으로 시작
    row = column = 0

    # 진행방향 설정 (0-오른쪽, 1-아래쪽, 2-왼쪽, 3-위쪽)
    direction = 0

    # 3
    # 00 - 1 / 01 - 2 / 02 - 3 / 03 -
    for num in range(1, number**2+1):
        # 보드칸에 값 입력
        board[row][column] = num
        
        # 진행 방향에 따라 row, column 의 값들에 값 추가
        row += dr[direction]
        column += dc[direction]

        # 다음에 값을 입력한 보드칸에 대한 조건
        # 다음 인덱스 값들이 음수이거나, 인덱스 범위 초가시
        # 혹은 다음 보드칸에 0이 아닌 다른 숫자가 있는 경우
        # 인덱스 이동을 다시 되돌리고, 방향을 전환시킴
        if row < 0 or row >= number or column < 0 or column >= number or board[row][column] != 0:
            # 실행취소
            row -= dr[direction]
            column -= dc[direction]

            # 방향 전환
            direction = (direction + 1) % 4

            # 다음 보드칸으로 진행
            row += dr[direction]
            column += dc[direction]

    print(f'#{index}')
    for p in board:
        print(*p)