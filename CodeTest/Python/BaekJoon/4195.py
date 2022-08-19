import sys
sys.stdin = open('input.txt')


# from 그룹원들의 번호를 to 그룹으로 변경
def move_group(to_group, from_group):
    for e in group[from_group]:
        friends[e] = to_group


T = int(sys.stdin.readline())

for _ in range(T):
    F = int(sys.stdin.readline())

    # 이름별 속한 그룹 번호
    friends = {}
    # 그룹별 속한 이름의 명단
    group = [set() for _ in range(F+1)]

    for i in range(1, F+1):
        a, b = sys.stdin.readline().split()

        # 이번에 처음 나온 친구 관계인 경우
        # 새롭게 등록
        if not friends.get(a, False) and not friends.get(b, False):
            friends[a], friends[b] = i, i
            group[i] = set((a, b))
        # 둘 다 이미 친구 그룹에 속해있는 경우
        elif friends.get(a, False) and friends.get(b, False):
            # 서로 다른 그룹일때만, 두개의 그룹을 합침
            if friends[a] != friends[b]:
                to_group, from_group = friends[a], friends[b]
                group[to_group].update(group[from_group])
                move_group(to_group, from_group)
                group[from_group].clear()
        # 둘 중 하나만 그룹에 속한 경우, 존재하는 그룹으로 귀속
        else:
            group_number = friends.get(a, False) or friends.get(b, False)
            friends[a], friends[b] = group_number, group_number
            group[group_number].update([a, b])

        print(len(group[friends[a]]))
