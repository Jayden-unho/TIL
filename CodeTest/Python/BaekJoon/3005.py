import sys
from functools import reduce
sys.stdin = open('input.txt')


def register_word(prev: set, curr: set) -> set:
    # 각 집합 내의 요소들에서 2글자 이상들만 서로 합치는 함수
    return prev | set(filter(lambda x: len(x) >= 2, curr))


# 행, 열
R, C = map(int, sys.stdin.readline().split())
rows = [sys.stdin.readline().rstrip() for _ in range(R)]
cols = list(map(lambda x: ''.join(x), zip(*rows)))

# '#' 을 기준으로 단어 구분, 중복 제거를 위해 집합 사용
words_li = map(lambda x: set(x.split('#')), rows + cols)
# 단어가 2자리 이상만, 걸러서 하나의 집합으로 합치기
words = reduce(register_word, words_li, set())
# 사전순 정렬
answer = sorted(words)[0]

print(answer)
