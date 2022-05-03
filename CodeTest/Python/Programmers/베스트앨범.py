def solution(genres, plays):
    genre_dict = {}                                                     # 장르별 플레이 리스트, 장르: {플레이리스트, 총 플레이 시간}
    genre_plays = []                                                    # 장르별 총 플레이 시간
    answer = []                                                         # 정답 리스트

    for idx in range(len(genres)):                                      # 입력으로 주어지는 모든 장르들 반복
        genre = genres[idx]
        play = plays[idx]

        if not genre_dict.get(genre, False):                            # 아직 나온적 없는 장르라면, 딕셔너리에 키값과 기본 값 추가
            genre_dict[genre] = {'plays': [], 'total_play': 0}

        genre_dict[genre]['plays'].append((play, idx))                  # 현재 노래 플레이 시간, 고유 번호
        genre_dict[genre]['total_play'] += play                         # 현재 노래 플레이 시간을 총 플레이 시간에 추가

    for k, v in genre_dict.items():                                     # 장르별로 반복하며
        genre_plays.append((k, v['total_play']))                        # (장르, 총 플레이시간) 형태로 리스트에 추가
    
    genre_plays.sort(key=lambda x: x[1], reverse=True)                  # 총 플레이시간을 기준으로 내림차순 정렬

    for genre, _ in genre_plays:
        play = sorted(genre_dict[genre]['plays'], key=lambda x: x[1], reverse=True)     # 노래 고유번호 기준으로 내림 차순
        play = sorted(play, key=lambda x: x[0])                                         # 노래 플레이 시간 기준으로 오름 차순
                                                                                        # 가장 많이 플레이 노래 오름차순으로 정렬되고, 고유번호 기준으로 내림차순 정렬됨
        idx = 2                             # 한 장르에 최대 2개 모음
        while idx > 0 and play:             # 두개 아직 안넣었거나, 넣을 노래가 있을때 반복
            answer.append(play.pop()[1])    # 위에서 정렬한 노래를 가장 뒤에서부터 꺼내와서 정답에 저장
            idx -= 1

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop", "pop"], [500, 600, 150, 800, 2500, 600]))