import sys



def paper_divide(start_x, start_y, length):
    set_num = paper[start_y][start_x]
    sign = True

    for i in range(start_y, start_y + length):
        for j in range(start_x, start_x + length):
            if paper[i][j] != set_num:
                sign = False
                break
        if sign == False:
            break
    
    # Base Case
    if sign == True:
        answer[set_num] += 1
    else:
        for i in range(3):
            for j in range(3):
                paper_divide(start_x + j*length//3, start_y + i*length//3, length//3)



number = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(number)]

answer = {
    -1 : 0,
    0 : 0,
    1 : 0,
}

paper_divide(0, 0, number)

for n in answer:
    print(answer[n])