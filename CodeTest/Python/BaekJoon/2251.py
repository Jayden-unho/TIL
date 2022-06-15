import sys
sys.stdin = open('input.txt')

def solution(case):
    stack = case
    water = [0, 0, buckets[2]]

    # print('------------------------')
    # print(f'start : {water}')
    while stack:
        t1, t2 = stack.pop()
        # print(f't1 : {t1} | t2 : {t2}')
        can_move = min(buckets[t1], buckets[t2], water[t1])
        water[t2] += can_move
        water[t1] -= can_move
        # print(f'move : {can_move} | water : {water}')

    if not water[0]:
        answer.add(water[2])
    
    
buckets = list(map(int, sys.stdin.readline().split()))
answer = {buckets[2]}

for case in [[[2, 1]], [[0, 1], [2, 0]], [[0, 2], [2, 1], [2, 0]], [[0, 1], [1, 2], [2, 0], [2, 1]], [[0, 2], [1, 0], [2, 1]]]:
    solution(case)

print(*sorted(answer))
# 1 C->B                            | C->B
# 2 C->A & A->B                     | C->A->B
# 3 C->A & C->B & A->C              | C->A, C->B, A->C
# 4 C->B & C->A & B->C & A->C       | C->B, C->A, B->C, A->B