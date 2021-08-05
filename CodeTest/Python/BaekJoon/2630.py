import sys


'''
재귀함수
잘린 종이가 하나의 색만 있으면 Base Case로 return 1
하나의 색이 아니면 재귀
'''

def colored_paper(coordinate, length):
    x, y = coordinate[0], coordinate[1]
    
    my_sum = 0
    for i in range(length):
        for j in range(length):
            my_sum += paper[x+i][y+j]
    
    #Base Case
    if my_sum == 0:
        answer[0] += 1
    elif my_sum == length**2:
        answer[1] += 1
    else:
        colored_paper([x, y], length//2)    # 왼쪽 위
        colored_paper([x, y + length//2], length//2)         # 오른쪽 위  
        colored_paper([x + length//2, coordinate[1]], length//2)        # 왼쪽 아래
        colored_paper([x + length//2, y + length//2], length//2)            # 오른쪽 아래




number = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(number)]
answer = [0, 0] # idx 0 - white / idx 1 - blue


colored_paper([0, 0], number)

for e in answer:
    print(e)