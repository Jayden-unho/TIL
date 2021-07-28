import sys

testCase = int(sys.stdin.readline())

for _ in range(testCase):
    number, target = map(int, sys.stdin.readline().split())
    importance_list = list(map(int, sys.stdin.readline().split()))
    answer = []
    docu = {}

    # 딕셔너리에 할당 키:순서 / 값:중요도
    for i in range(number):
        docu[i] = importance_list[i]

    while docu:
        max_importance = max(docu.values())
        