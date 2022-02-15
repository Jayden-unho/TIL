def solution(user_id, banned_id):
    answer = set()                                                          # 제재 아이디 가능한 경우들 집합
    user_id = list(sorted(user_id, key=lambda x: (len(x), x)))              # 유저 아이디를 길이순, 알파벳순으로 정렬
    cases = [[] for _ in range(len(banned_id))]                             # 불량 사용자별 가능한 유저 아이디 경우

    for ban_idx in range(len(banned_id)):                                   # 불량 유저 아이디를 하나씩 탐색
        banned = banned_id[ban_idx]
        L = len(banned)
        for user in user_id:                                                # 유저 아이디 앞에서 부터 탐색
            if len(user) == L:                                              # 유저 아이디가 불량 유저 아이디와 길이가 같을때
                idx = 0
                while idx < L:                                              # 해당 유저가 제재 가능한 경우에, cases 리스트에 각 인덱스별로 추가
                    if banned[idx] != user[idx] and banned[idx] != '*':
                        break
                    idx += 1
                else:
                    cases[ban_idx].append(user)
            elif len(user) > L:                                             # 유저 아이디의 길이가 길면 이후 유저 아이디 탐색 종료
                break
    
    def comb(n, ans):                               # 제재 아이디 가능한 조합 탐색
        if n >= len(banned_id):
            answer.add(tuple(sorted(ans)))          # 제재 가능한 경우 추가
            return

        for k in range(len(cases[n])):              # cases 의 각 요소들의 길이만큼 반복
            if cases[n][k] not in ans:              # 같은 이름이 없는 경우에만 추가하며, 재귀 탐색
                comb(n+1, ans+[cases[n][k]])

    comb(0, [])

    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))