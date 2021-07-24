import sys

def star_print(number, a=0, b=0):
    '''
    3을 제외한 3의 거듭제곱이 들어오는 경우 - number//3 사이즈의 정사각형을 9개 만들어서 함수 호출, 어떤 위치의 정사각형을 가져왔는지 알기 위해 ,매개변수 a,b 를 사용 (초기값은 0,0 으로 설정)
    a와 b의 값은 정사각형의 첫번째 인덱스 값으로 나타냄
    '''
    # global 사용으로 리스트의 값을 바로 수정함
    global board

    # Base Case
    # 3x3 사이즈의 정사각형인 경우, 정가운데 부분 공백으로 설정
    if number == 3:
        for x in range(a+1, a+2):
            for y in range(b+1, b+2):
                board[x][y] = ' '
    # 3 제외, 3의 거듭제곱이 들어오는 경우 
    else:
        # a - (잘린) 정사각형의 첫번째 인덱스
        # a+number - (잘린) 정사각형의 가로 사이즈
        # number//3 - 입력된 숫자의 하위 거듭제곱만큼 잘라야 함
        for i in range(a, a+number, number//3):
            for j in range(b, b+number, number//3):
                # 9개의 정사각형 도형 중 가운데 도형이 선택이 되는 경우, 모두 공백처리
                if i == a+number//3 and j == b+number//3:
                    for x in range(a+number//3, a+number//3*2):
                        for y in range(b+number//3, b+number//3*2):
                            board[x][y] = ' '
                    # 공백이 되는 칸은 밑에 재귀함수로 들어갈 필요 없음
                    continue
                # 숫자의 하위 거듭제곱의 숫자와 정사각형의 첫번째 인덱스 값 넘김
                star_print(number//3, a=i, b=j)



number = int(sys.stdin.readline())

# 주어진 숫자만큼 크기의 2차원 배열을 만듦, 모든 배열값은 * 가 출력되는 상태로
board = [['*']*number for _ in range(number)]
star_print(number)

for i in range(number):
    for j in range(number):
        print(board[i][j],end='')
    print()