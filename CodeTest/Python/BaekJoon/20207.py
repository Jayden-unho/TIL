import sys
sys.stdin = open("input.txt")

answer = 0
schedule = {}

# 시작/종료 날짜별 증감량 기록
for _ in range(int(sys.stdin.readline())):
    S, E = map(int, sys.stdin.readline().split())
    schedule[S] = schedule.get(S, 0) + 1
    schedule[E+1] = schedule.get(E+1, 0) - 1

# 일정 마지막 종료 일 구해서 누적합 배열 생성
last_date = max(schedule.keys())
acc_schedule = [0] * (last_date + 1)

# 직사각형 넓이를 구하기 위한 너비/높이
height = 0
width = 0
for idx in range(1, last_date+1):
    num = acc_schedule[idx-1] + schedule.get(idx, 0)

    # 오늘 일정이 비어있다면, 직사각형 코팅지 끊김
    # 지금까지 코팅지 너무 구하기 및 너비/높이 리셋
    if not num:
        answer += width * height
        width = 0
        height = 0
    # 일정이 연속된다면, 코팅지 넓이 계산을 위한 너비/높이 변화
    else:
        width += 1
        height = max(height, num)

    # 누적합 저장
    acc_schedule[idx] = num

print(answer)
