MONTH_DAY = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

testCase = int(input())

for i in range(1, testCase+1):
    answer = 0
    answer2 = 0
    fir_mon, fir_day, sec_mon, sec_day = map(int, input().split())

    # for문 이용한 풀이
    for i in range(fir_mon, sec_mon):
        answer += MONTH_DAY[i]
    answer += sec_day + 1 - fir_day

    # while문 이용한 풀이
    while fir_mon < sec_mon:
        answer2 += MONTH_DAY[fir_mon]
        fir_mon += 1
    answer2 += sec_day + 1 - fir_day

    print(f'#{i} {answer}')
    print(f'#{i} {answer2}')