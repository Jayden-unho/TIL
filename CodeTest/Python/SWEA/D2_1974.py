ONE_TO_NINE = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def lineChk(sudoku):
    for i in range(9):
        width_chk = []
        height_chk = []
        for j in range(9):
            width_chk.append(sudoku[i][j])
            height_chk.append(sudoku[j][i])

        if ONE_TO_NINE != sorted(width_chk):
            return 0
        elif ONE_TO_NINE != sorted(height_chk):
            return 0    
    return 1

def squareChk(sudoku):
    for i in range(0,9,3):
        for j in range(0,9,3):
            square_chk = []
            for a in range(i, i+3):
                for b in range(j, j+3):
                    square_chk.append(sudoku[a][b])
            if ONE_TO_NINE != sorted(square_chk):
                return 0
    return 1


testCase = int(input())

for i in range(1, testCase+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    
    answer = lineChk(sudoku)
    if answer == 1:
        answer = squareChk(sudoku)

    print(f'#{i} {answer}')