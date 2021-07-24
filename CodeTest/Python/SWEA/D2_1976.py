testCase = int(input())

for i in range(1, testCase+1):
    hour1, minutes1, hour2, minutes2 = map(int, input().split())

    ans_hour = hour1 + hour2
    ans_min = minutes1 + minutes2

    # 분이 60 이상이면
    if ans_min >= 60:
        ans_hour += 1
        ans_min -= 60
    
    # 시가 13 이상이면
    if ans_hour >= 13:
        ans_hour -= 12

    print(f'#{i} {ans_hour} {ans_min}')