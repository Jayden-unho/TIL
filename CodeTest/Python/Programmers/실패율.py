def solution(level, stages):
    answer = []
    fail_ratio = []

    stages.sort(reverse=True)

    for n in range(1, level+1):
        challenge = 0   # 현재 레벨에 도전하고 있는 인원
        for idx in range(len(stages)-1, -1, -1):
            if stages[idx] == n:
                challenge += 1
            else:
                break

        fail_ratio.append(challenge / len(stages))
        stages = stages[:idx+1]

    fail_ratio = enumerate(fail_ratio, start=1)
    fail_ratio = sorted(fail_ratio, key=lambda fail_ratio:fail_ratio[1], reverse=True)


    for e in fail_ratio:
        answer.append(e[0])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))