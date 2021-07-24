# 인터넷에 올라온 방법
import sys


input_height, input_width = map(int, sys.stdin.readline().split())
board = []  # 주어진 보드판
changeNumList = []   # 바꿔야할 횟수 담아두는 리스트 

# 값을 입력받아 일차원 배열에 저장
for _ in range(input_height):
    board.append(sys.stdin.readline().rstrip())
    print(board)

for a in range(input_height-7):
    for i in range(input_width-7):
        idx1 = 0
        idx2 = 0

        for b in range(a, a+8):
            for j in range(i, i+8):
                # 좌판에 블랙인 경우와 화이트인 경우 동시 검사
                if (j+b)%2 == 0:
                    if board[b][j] != 'W': idx1 += 1
                    if board[b][j] != 'B': idx2 += 1
                elif (j+b)%2 == 1:
                    if board[b][j] != 'B': idx1 += 1
                    if board[b][j] != 'W': idx2 += 1

        changeNumList.append(idx1)
        changeNumList.append(idx2)

print(min(changeNumList))

# 내가 생각한 방법
'''
import sys


# 0,0이 블랙인 경우
# i,j 의 합이 짝수이면 블랙, 홀수이면 화이트
def case1(li):
    count = 0
    for a in range(8):
        for b in range(8):
            if (a+b) % 2 == 0 and li[a][b] != 'B':
                count += 1
            elif (a+b) % 2 == 1 and li[a][b] != 'W':
                count += 1
    return count

# 0,0이 화이트인 경우
# i,j 의 합이 짝수이면 화이트, 홀수이면 블랙
def case2(li):
    count = 0
    for a in range(8):
        for b in range(8):
            if (a+b) % 2 == 0 and li[a][b] != 'W':
                count += 1
            elif (a+b) % 2 == 1 and li[a][b] != 'B':
                count += 1
    return count


height, width = map(int, sys.stdin.readline().split())
# 입력 받은 값을 한줄로 읽어서 2차원 배열로 만듦
board = [list(sys.stdin.readline().rstrip()) for _ in range(height)]
min_change = 64
send_board = []
tmp = 0

for i in range(height-7):
    for j in range(width-7):
        # 함수에 전송할 8*8 사이즈로 자른 보드들
        send_board = [k[j:j+8] for k in board[i:i+8]]


        tmp = case1(send_board)
        if min_change > tmp:
            min_change = tmp

        tmp = case2(send_board)
        if min_change > tmp:
            min_change = tmp
print(min_change)
'''