import sys
sys.stdin = open('input.txt')


def get_value(person):
    """
    person 사람이 내야하는 손동작 번호 반환
    만약 지우라면, None 반환
    """
    if person == 0:
        return None
    return people[person][idxs[person]]


def sol(pair, selected):
    global answer

    if answer == 1:
        return
    elif wins[0] == K:
        answer = 1
        return
    elif wins[1] == K or wins[2] == K:
        return

    l, r = sorted(pair)
    left, right = get_value(l), get_value(r)
    idxs[l], idxs[r] = idxs[l]+1, idxs[r]+1
    other = set(range(3)) - set(pair)

    def inner(cb):
        """
        반복을 줄이기 위한 내부 함수
        """
        winner = l if infos[left][right] == 2 else r
        wins[winner] += 1
        cb(other | {winner})
        wins[winner] -= 1

    if l:  # 경희 vs 민호
        inner(lambda next_pair: sol(next_pair, selected))
    else:  # 지우 vs 경희 또는 민호
        for left in range(N):
            if left not in selected:  # 지우가 이전에 내지 않은 손동작인 경우
                inner(lambda next_pair: sol(next_pair, selected | {left}))

    idxs[l], idxs[r] = idxs[l]-1, idxs[r]-1


N, K = map(int, sys.stdin.readline().split())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

people = [[] for _ in range(3)]
people[1] = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))  # 경희
people[2] = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))  # 민호

answer = 0
idxs = [0, 0, 0]  # 경희와 민호가 내는 손동작 순서 인덱스
wins = [0, 0, 0]  # 게임 진행 중 몇 번 승리인지 카운트

sol((0, 1), set())

print(answer)
