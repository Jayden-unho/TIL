'''
재귀 및 분할정복 활용
'''

import sys



def solution(row, col, length):             # 제일 왼쪽 위 시작 좌표, 길이
    tmp_sum = 0                             # 해당 구역의 합을 저장하는 임시 변수
    for i in range(row, row+length):        
        for j in range(col, col+length):
            tmp_sum += int(image[i][j])     # 해당 구역의 숫자들을 모두 합함

    #Base Case
    if not tmp_sum or tmp_sum == length**2: # 해당 구역의 숫자들이 모두 0 이거나 1일때
        return image[row][col]              # 해당 구역의 숫자 반환

    # 0과 1의 숫자가 섞여 있을때, 해당 구역을 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래로 나누어 재귀 호출
    return '(' + solution(row, col, length//2) + solution(row, col+length//2, length//2) + solution(row+length//2, col, length//2) + solution(row+length//2, col+length//2, length//2) + ')'



n = int(sys.stdin.readline())
image = [sys.stdin.readline() for _ in range(n)]

answer = solution(0, 0, n)
print(answer)