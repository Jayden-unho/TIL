def solution(lines):
    answer = 0                                  # 초당 최대 처리량
    cnt = 0                                     # 특정 시간대 처리량
    time_line = {}                              # 시간 테이블 - 키: 시간(ms) / 값: 시작 또는 완료 여부 (-1, 1)

    for line in lines:                          # 로그 데이터
        date, time, duration = line.split(' ')  # 날짜, 시간, 처리 시간
        end_ms = int(time[:2]) * 3600000 + int(time[3:5]) * 60000 + int(time[6:8]) * 1000 + int(time[9:])       # 요청 시간 (ms)
        start_ms = end_ms - int(duration[0]) * 1000 - (int(duration[2:-1]) if len(duration) > 2 else 0) + 1     # 완료 시간 (ms)
        end_ms += 1000                                          # 1초간 최대 처리량을 구해야 하므로 완료 시간을 1초 추가

        time_line[start_ms] = time_line.get(start_ms, 0) + 1    # 시작 시간을 키로 해서 값은 1
        time_line[end_ms] = time_line.get(end_ms, 0) - 1        # 완료 시간을 키로 해서 값은 -1

    for t in sorted(time_line.keys()):      # 키값들을 오름차순 정렬하여 시간 순서대로 반복
        cnt += time_line[t]                 # 값들 누적시키기
        answer = max(answer, cnt)           # 최대 처리량 구하기

    return answer


print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))