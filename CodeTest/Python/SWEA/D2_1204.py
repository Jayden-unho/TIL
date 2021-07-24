import sys
sys.stdin = open('input.txt', 'r')

testCase = int(input())


for _ in range(testCase):
    index = int(input())

    # 모든 점수들을 리스트에 담는다
    scores = list(map(int, input().split()))
    # 중복이 제거된 점수들만 따로 모음
    scores_set = list(set(scores))
    answer = []

    # 각 점수별로 몇명이 있는지 리스트 형태로 새로 만듦 (점수, 동점 몇명인지)
    for score in scores_set:
        answer.append(list([score, scores.count(score)]))

    # 동점이 많은 숫자를 기준으로 내림차순, 최빈수가 여러개인 경우 대비하여 2차적으로 점수도 내림차순 정렬
    answer = sorted(answer, key=lambda li:(li[1], li[0]), reverse=True)
    print(f'#{index} {answer[0][0]}')