def solution(board, skills):
    answer = 0
    N = len(board)                      # 행
    M = len(board[0])                   # 열

    variation_board = [[0] * (M+1) for _ in range(N+1)]     # 변화량을 기록할 2차원 배열 (누적합을 이용할것이기에 0행과 0열은 모두 0의 값을 적용)

    for skill in skills:
        type, r1, c1, r2, c2, degree = skill                # 스킬의 종류, 왼쪽 위 모서리 좌표, 오른쪽 아래 모서리 좌표

        if type == 1:                                       # 공격인 경우, 음수이므로 -1을 곱함
            degree *= -1

        variation_board[r1+1][c1+1] += degree               # 왼쪽 위의 모서리에 변화량 기록
        if c2+2 <= M:                                       # 오른쪽 위의 모서리 다음 좌표에 변화량의 -1을 곱한 값 기록
            variation_board[r1+1][c2+2] += -degree
        if r2+2 <= N:                                       # 왼쪽 아래 모서리
            variation_board[r2+2][c1+1] += -degree
        if r2+2 <= N and c2+2 <= M:                         # 오른쪽 아래 모서리
            variation_board[r2+2][c2+2] += degree

    for i in range(1, N+1):                                 # 2차원 배열 반복하며 변화량 계산
        for j in range(1, M+1):
            variation_board[i][j] = variation_board[i-1][j] + variation_board[i][j-1] - variation_board[i-1][j-1] + variation_board[i][j]
    
    for i in range(N):                                      # 2차원 배열의 초기값 추가
        for j in range(M):
            if variation_board[i+1][j+1] + board[i][j] > 0:
                answer += 1

    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))