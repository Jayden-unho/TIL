import sys
from itertools import permutations
sys.stdin = open('input.txt')


def sol(pair):
    global answer

    # 지우 승
    if wins[0] == K:
        answer = 1
        return
    # 다른 사람 승
    elif wins[1] == K or wins[2] == K:
        return
    # 지우가 모두 다른걸 냈지만 우승 못한 경우
    elif idxs[0] == N:
        return

    l, r = pair  # 왼쪽 사람, 오른쪽 사람
    l_idx, r_idx = idxs[l], idxs[r]  # 각 사람이 낼 손동작 배열의 인덱스
    left, right = people[l][l_idx], people[r][r_idx]  # 각 사람이 낼 손동작 번호

    # 왼쪽 승
    if infos[left][right] == 2:
        wins[l] += 1
        winner = {l}
    # 오른쪽 승
    else:
        wins[r] += 1
        winner = {r}

    # 대결 진행했으므로 손동작 배열의 인덱스 증가
    idxs[l] += 1
    idxs[r] += 1

    # 다음 대결 상대 구하기
    other = set(range(3)) - set(pair)
    new_pair = sorted(other | winner)

    sol(new_pair)


N, K = map(int, sys.stdin.readline().split())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

people = [[] for _ in range(3)]
people[1] = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))  # 경희
people[2] = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))  # 민호

answer = 0
# 지우가 모든 손동작을 다르게 낼 수 있는 경우들 탐색
for jiwoo in permutations(range(N), N):
    people[0] = jiwoo

    idxs = [0, 0, 0]
    wins = [0, 0, 0]
    sol((0, 1))
    if answer:
        break

print(answer)
