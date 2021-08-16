'''
재귀함수
2차원 배열에 숫자를 순차적으로 입력
-> 메모리 및 시간 초과

구하려는 좌표값을 토대로 좌표가 포함되는 영역을 구하여 영역의 숫자를 구함
'''

def sector(x, y, length, start_number):                         # x,y - start coordinate / length - square length / start_number - square left_top number
    global r, c    

    #Base Case
    if length == 1:
        return start_number

    else:                                                       # 사각형을 4등분 했을때, 구해야할 좌표가 4개의 구역중 어디에 속하는지에 따라 실행됨
        if r < (y+length)//2 and c < (x+length)//2:             # left_top / 왼쪽 위에서 시작 좌표, 길이가 반으로 줄어듦, 왼쪽 위에 시작하는 숫자
            return sector(x, y, length//2, start_number)
        elif r < (y+length)//2 and c >= (x+length)//2:          # right_top / 오른쪽 위에서 시작 좌표, 길이가 반으로 줄어듦, 오른쪽 위에 시작하는 숫자
            return sector(x+length, y, length//2, start_number + (length//2)**2)
        elif r >= (y+length)//2 and c < (x+length)//2:          # left_bottom
            return sector(x, y+length, length//2, start_number + ((length//2)**2)*2)
        elif r >= (y+length)//2 and c >= (x+length)//2:         # right_bottom
            return sector(x+length, y+length, length//2, start_number + ((length//2)**2)*3)



import sys


n, r, c = map(int, sys.stdin.readline().split())
length = 2 ** n

answer = sector(0, 0, length, 0)
print(answer)