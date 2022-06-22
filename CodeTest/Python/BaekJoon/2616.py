import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                               # 객차의 개수
carriage = list(map(int, sys.stdin.readline().split()))     # 객차별 사람 수
can_carriage = int(sys.stdin.readline())                    # 소형 기관차가 끌 수 있는 최대 객차 수

acc_people = [0]                                # 사람 수 누적합
dp = [[0] * (N+1) for _ in range(4)]            # 객차 선택에 따른 최대 사람 수 DP

for i in range(1, N+1):                         # 첫 객차부터 누적합 구하기
    acc = acc_people[-1] + carriage[i-1]
    acc_people.append(acc)

for i in range(1, 4):                           # 소형 기관차 사용하는 개수 (총 3개)
    for j in range(i * can_carriage, N+1):      # 끌고 가는 객차 시작 번호
        people = acc_people[j] - acc_people[j-can_carriage]             # 현재 객차를 시작으로 끌었을 때 최대 인원수
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-can_carriage] + people)    # 이전 경우 / 소형 기관차 하나 덜 썼을때 최대 인원 수와 기관차 하나 더 써서 추가된 인원수 합
                                                                        # 둘 중에 더 큰 값 기록
print(dp[-1][-1])           # 기관차 3개를 사용하고, 최대로 이송 가능한 인원 수 출력