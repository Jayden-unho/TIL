import sys
sys.stdin = open('input.txt')

def solution(n):                        # 타자 순서 정하는 함수
    if n == 9:                          # 9번 타자까지 모두 순서를 정했다면
        inning(0, 0, 0)                 # 시뮬레이션 시작
        return
    
    for i in range(9):
        if number_player[i] == -1:      # 현재 순번에 타자가 없다면
            number_player[i] = n        # 타자 순번 지정
            solution(n+1)               # 다음 타자의 순번 정하기
            number_player[i] = -1

def inning(n, ans, turn):               # 이닝 시뮬레이션 함수 (이닝 번호, 현재까지 점수, 현재 순서)
    global answer

    if n == N:
        answer = max(answer, ans)       # 높은 점수 저장
        return

    score, remain_out, base1, base2, base3 = 0, 3, 0, 0, 0      # 현재 이닝의 점수, 남은 아웃 카운트, 1루, 2루, 3루
    while remain_out > 0:                               # 아웃 카운트 남았으면 진행
        player = number_player[turn]                    # 현재 순서인 선수

        if not scores[n][player]:                       # 아웃이라면, 아웃카운트 증가
            remain_out -= 1                             
        elif scores[n][player] == 1:                    # 안타라면, 3루 점수 득점
            score += base3                              # 각 1루씩 전진
            base1, base2, base3 = 1, base1, base2
        elif scores[n][player] == 2:                    # 2루타라면, 2루, 3루 점수 득점
            score += base2 + base3                      # 각 2루씩 전진
            base1, base2, base3 = 0, 1, base1
        elif scores[n][player] == 3:                    # 3루타라면, 1,2,3루 점수 득점
            score += base1 + base2 + base3              # 각 3루씩 전진
            base1, base2, base3 = 0, 0, 1
        elif scores[n][player] == 4:                    # 홈런이라면 타자 및 모든 주자 득점
            score += base1 + base2 + base3 + 1          # 1,2,3루 모두 비어있게 설정
            base1, base2, base3 = 0, 0, 0

        turn = (turn + 1) % 9                           # 턴 증가
    
    inning(n+1, ans+score, turn)                        # 다음 이닝 진행

N = int(sys.stdin.readline())                                               # 이닝 수
scores = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]   # 이닝별 선수들 타자 정보
number_player = [-1] * 9                                                    # 타순별 선수 번호
number_player[3] = 0                                                        # 1번 타자는 4번 타자로 고정
answer = 0

solution(1)                     # 2번 타자부터 타순 정하기

print(answer)


# import sys
# sys.stdin = open('input.txt')

# def solution(n):
#     global turn

#     if n == 9:
#         turn = 0
#         inning(0, 0)
#         return
    
#     for i in range(9):
#         if number_player[i] == -1:
#             number_player[i] = n
#             solution(n+1)
#             number_player[i] = -1

# def inning(n, ans):
#     global answer, turn

#     if n == N:
#         if ans > answer:
#             answer = ans
#         return

#     base = [0] * 3
#     remain_out = 3
#     score = 0
#     while remain_out > 0:
#         if turn == 9:
#             turn = 0
        
#         player = number_player[turn]

#         num = scores[n][player]
#         if not num:
#             remain_out -= 1
#         else:
#             for j in range(2, -1, -1):
#                 if j + num > 2 and base[j]:
#                     score += 1

#                 if j >= num:
#                     base[j] = base[j-num]
#                 else:
#                     base[j] = 0

#             if num < 4:
#                 base[num-1] = 1
#             else:
#                 score += 1

#         turn += 1
    
#     inning(n+1, ans+score)

# N = int(sys.stdin.readline())                                       # 이닝 수
# scores = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]   # 이닝별 선수들 타자 정보
# number_player = [-1] * 9                                            # 타순별 선수 번호
# number_player[3] = 0
# answer = 0

# turn = 0

# solution(1)

# print(answer)