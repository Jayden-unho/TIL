import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())                   # 테스트 케이스 개수

for _ in range(T):
    N = int(sys.stdin.readline())               # 전화번호의 개수
    li = list(sorted([sys.stdin.readline().strip() for _ in range(N)]))     # 전화번호를 숫자 순으로, 길이 순으로 정렬
    answer = False                                  # 일관성 있는 목록인지 판별 여부, 일관성이 없는 경우 True 가 됨

    for i in range(N):                              # 앞에 번호들부터 순서대로 반복
        next_num = False                            # 다음 숫자를 탐색하는지 판별하는 신호 변수
        for j in range(i+1, N):                     # 비교하는 기준 숫자의 다음 번호부터
            if next_num:
                break

            for k in range(len(li[i])):             # 가장 앞 글자의 숫자부터 비교
                if int(li[i][k]) < int(li[j][k]):   # 현재 비교하는 숫자가 비교하는 번호가 더 크다면, 기준 번호를 다음 번호로 넘김
                    next_num = True
                    break
                elif int(li[i][k] > li[j][k]):      # 현재 비교하는 숫자가, 기준 숫자가 더 크다면
                    break                           # 비교하는 번호 다음 번호로 이동
            else:                                   # 일관성 있는 숫자인 경우
                answer = True                       # 이후 탐색 모두 종료
        
        if answer:              # 출력
            print('NO')
            break
    else:
        print('YES')