def solution(infos, query):
    answer = []
    people = {}

    for info in infos:
        tmp = info.split(' ')
        
        people[tmp[0]] = people.get(tmp[0], {})
        people[tmp[0]][tmp[1]] = people[tmp[0]].get(tmp[1], {})
        people[tmp[0]][tmp[1]][tmp[2]] = people[tmp[0]][tmp[1]].get(tmp[2], {})
        people[tmp[0]][tmp[1]][tmp[2]][tmp[3]] = people[tmp[0]][tmp[1]][tmp[2]].get(tmp[3], []) + [tmp[4]]

    for q in query:
        tmp_answer = 0
        tmp = q.split(' and ')
        tmp += tmp.pop().split(' ')

        for e in tmp:
            if e != '-':
                

    return answer

print(solution([
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"
    ], [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"
    ]))