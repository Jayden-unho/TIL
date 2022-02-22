# def solution(play_time, adv_time, logs):
#     def time_to_seconds(s):                                         # 문자열 시간을 초로 바꾸어 주는 함수
#         return int(s[:2]) * 3600 + int(s[3:5]) * 60 + int(s[6:8])

#     watch_table = {}                                # 사람들 시청 정보 - 키: 시작 또는 종료 시간, 값: 1은 시청 시작, -1은 시청 종료
#     answer_play_time = 0
#     answer = 0

#     play_time_seconds = time_to_seconds(play_time)
#     adv_time_seconds = time_to_seconds(adv_time)

#     cnt = 0
#     for log in logs:
#         start, end = log.split('-')
        
#         start_seconds = time_to_seconds(start)
#         end_seconds = time_to_seconds(end)
        
#         watch_table[start_seconds] = watch_table.get(start_seconds, 0) + 1
#         watch_table[end_seconds] = watch_table.get(end_seconds, 0) - 1
    
#     watch_cnt = [0] * (play_time_seconds - adv_time_seconds + 1)


#     for t in range(play_time_seconds - adv_time_seconds, -1, -1):
#         tmp_answer = 0
#         cnt = 0
#         pre_t = t
#         for k in sorted(watch_table.keys()):
#             if t <= k <= t + adv_time_seconds:
#                 tmp_answer += (k - pre_t) * cnt
#                 pre_t = k
#             elif k > t + adv_time_seconds:
#                 tmp_answer += (t + adv_time_seconds - pre_t) * cnt
#                 break
#             cnt += watch_table[k]
        
#         if answer_play_time <= tmp_answer:
#             answer_play_time = tmp_answer
#             answer = t

#     return f'{answer//3600 if answer//3600 >= 10 else f"0{answer//3600}"}:{answer%3600//60 if answer%3600//60 >= 10 else f"0{answer%3600//60}"}:{answer%60 if answer%60 >= 10 else f"0{answer%60}"}'

def solution(play_time, adv_time, logs):
    def time_to_seconds(s):                                         # 문자열 시간을 초로 바꾸어 주는 함수
        return int(s[:2]) * 3600 + int(s[3:5]) * 60 + int(s[6:8])

    play_time_seconds = time_to_seconds(play_time)                  # 영상 총 길이 초로 변환
    adv_time_seconds = time_to_seconds(adv_time)                    # 광고 시간 초로 변환
    watch_table = [0] * (play_time_seconds + 2)                     # 각 시간대별 시청자 수, 누적합 리스트
    max_play_time = 0                                               # 광고 이윤이 많이 남는 시간양
    answer = 0                                                      # 광고 이윤이 많이 남는 시작 시간
    
    for log in logs:                                                # 시청 기록들 하나씩 반복
        start, end = log.split('-')                                 # 시청 시작 시간, 종료 시간

        start_seconds = time_to_seconds(start)                      # 초로 변환
        end_seconds = time_to_seconds(end)

        watch_table[start_seconds + 1] += 1                         # 시청 시작 시간 인덱스에는 + 1
        watch_table[end_seconds + 1] -= 1                           # 시청 종료 시간 인덱스에는 - 1

    for _ in range(2):                                                  # 반복 1회 - 각 시간대별 몇명이 시청중인지 구하기
        for idx in range(1, play_time_seconds + 2):                     # 반복 2회 - 시간대별 시청중인 기록을 누적합으로 구하기
            watch_table[idx] = watch_table[idx-1] + watch_table[idx]
    
    for t in range(play_time_seconds-adv_time_seconds, -1, -1):             # 광고를 뒤에서부터 앞으로 탐색 시작
        tmp_play_time = watch_table[t+adv_time_seconds] - watch_table[t]    # 광고 이윤 시간 = 종료시 누적합 - 시작시 누적합
        if max_play_time <= tmp_play_time:                                  # 이윤이 같거나 더 많으면 새로 갱신
            max_play_time = tmp_play_time
            answer = t
            
    return f'{str(answer//3600).zfill(2)}:{str(answer%3600//60).zfill(2)}:{str(answer%60).zfill(2)}'    # 출력


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))