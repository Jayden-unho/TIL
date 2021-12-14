def trans(t):
    return int(t[:2])*60 + int(t[3:])


def solution(n, t, m, timetable):
    answer = ''
    idx = 0

    trans_timetable = list(sorted((map(trans, timetable))))

    for bus in range(540, 540+(t*n), t):
        boarding = m
        while True:
            if idx == len(timetable) or bus < trans_timetable[idx] or not boarding:
                break
            print(bus, trans_timetable[idx], boarding)
            
            boarding -= 1
            idx += 1

    
    return answer

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))