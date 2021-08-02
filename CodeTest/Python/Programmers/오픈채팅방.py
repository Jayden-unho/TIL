def solution(record):
    tmp = []
    answer = []
    record = [e.split() for e in record]
    nickname_dict = {}

    # 출입 관리 및 닉네임 관리
    for e in record:
        if e[0] == 'Enter':
            nickname_dict[e[1]] = e[2]
            tmp.append(e[0:2])
        elif e[0] == 'Leave':
            tmp.append(e[0:2])
        elif e[0] == 'Change':
            nickname_dict[e[1]] = e[2]

    for e in tmp:
        if e[0] == 'Enter':
            answer.append(f"{nickname_dict[e[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{nickname_dict[e[1]]}님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))