def solution(n, t, m, timetable):
    answer = 0
    bus = 540                   # 버스의 첫 시작 시간 (분)
    waiting = 0                 # 기다리는 사람의 수
    time_line = []              # 사람들이 기다리기 시작하는 시간 리스트

    for time in timetable:                                  # 사람들 줄서는 시간들을 분으로 계산하여 분으로 바꾸어 저장
        minute = int(time[:2]) * 60 + int(time[3:])         
        time_line.append(minute)
    time_line.sort()                                        # 사람들 시작 시간이 순서대로 들어오지 않으므로 오름차순 정렬
    
    idx = 0
    for bus in range(540, 540 + n*t, t):                        # 버스 시간 순서대로 반복
        while idx < len(time_line) and time_line[idx] <= bus:   # 버스 도착하기전에 사람들이 도착하는 경우에
            waiting += 1                                        # 기다리는 사람 추가
            idx += 1                                        
        waiting -= m                                            # 버스 도착하면 m 명 사람을 태움
        
        if bus == 540 + t*(n-1):                                # 마지막 버스 도착하면 종료
            break
        waiting = max(0, waiting)                               # 기다리는 사람이 -가 되는 경우, 대기 인원이 아무도 없는 경우이므로 0명으로 세팅

    if waiting < 0:                                 # 마지막 버스에 바로 탈 수 있으면
        answer = bus                                # 버스 도착하는 시간에 도착하면 됨
    else:
        answer = time_line[idx-waiting-1] - 1       # 그 외, 마지막 버스에 마지막으로 탄 크루보다 1분만 빨리도착하면 됨

    return f'{answer//60 if answer//60 >= 10 else f"0{answer//60}"}:{answer%60 if answer%60 >= 10 else f"0{answer%60}"}'

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
print(solution(10, 1, 5, ["09:00", "09:00", "09:00", "09:00", "09:00"]))