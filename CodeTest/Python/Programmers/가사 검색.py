def solution(words, queries):
    start = {}                                          # 앞에 ? 가 붙은 경우를 저장
    end = {}                                            # 뒤에 ? 가 붙은 경우를 저장
    answer = []                                         # 정답 리스트 변수

    for word in words:                                  # 단어를 저장
        n = len(word)                                   # 단어의 길이
        
        if not start.get(n, False):                     # 현재 길이가 단어들이 없으면 새로운 객체 생성
            start[n] = {'cnt': 1}
            end[n] = {'cnt': 1}
        else:                                           # 현재 길이의 단어들이 기록되어 있으면 단어 카운트 증가
            start[n]['cnt'] += 1
            end[n]['cnt'] += 1

        start_dict = start[n]                           # 내부 객체
        end_dict = end[n]
        for i in range(n):                              # 단어 한글자씩 반복
            start_c = word[i]                           # 앞글자
            end_c = word[n-i-1]                         # 뒷글자

            if not start_dict.get(start_c, False):      # 동일한 글자가 나온적이 없으면, 객체 생성
                start_dict[start_c] = {'cnt': 1}
            else:
                start_dict[start_c]['cnt'] += 1         # 나온적 있으면 카운트 증가

            if not end_dict.get(end_c, False):
                end_dict[end_c] = {'cnt': 1}
            else:
                end_dict[end_c]['cnt'] += 1
            
            start_dict = start_dict[start_c]            # 다음 내부 탐색을 위함
            end_dict = end_dict[end_c]
    

    for query in queries:                               
        if query[0] == '?':                             # 앞에 ? 가 있는 경우
            query = query[::-1]                         # 단어 뒤집기
            if end.get(len(query), False):              
                end_dict = end[len(query)]
            else:                                       # 해당 글자수가 없으면
                answer.append(0)                        # 0 반환
                continue

            cnt = end[len(query)]['cnt']                # 해당 글자수의 단어 개수 초기 정의
            end_dict = end[len(query)]                  # 내부 객체
            for q in query:
                if end_dict.get(q, False):              # 다음 글자가 있는 경우
                    cnt = end_dict[q]['cnt']            # 개수 저장
                    end_dict = end_dict[q]              # 내부 객체 조회 위함
                else:
                    if q == '?':            
                        answer.append(cnt)              # 현재 글자가 ? 라면, 저장된 개수 반환
                    else:
                        answer.append(0)                # 해당 문자가 아예 없으면 0 반환
                    break

        else:
            if start.get(len(query), False):
                start_dict = start[len(query)]
            else:
                answer.append(0)
                continue

            cnt = start[len(query)]['cnt']
            for q in query:
                if start_dict.get(q, False):
                    cnt = start_dict[q]['cnt']
                    start_dict = start_dict[q]
                else:
                    if q == '?':
                        answer.append(cnt)
                    else:
                        answer.append(0)
                    break
                
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))


# def solution(words, queries):
#     cases = {}
#     answer = []

#     for word in words:
#         n = len(word)
        
#         cases['?' * n] = cases.get('?' * n, 0) + 1
#         for i in range(1, n):
#             left = ('?' * i) + word[i:]
#             right = word[:i] + ('?' * (n-i))
#             cases[left] = cases.get(left, 0) + 1
#             cases[right] = cases.get(right, 0) + 1
    
#     for query in queries:
#         answer.append(cases.get(query, 0))

#     return answer

# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))