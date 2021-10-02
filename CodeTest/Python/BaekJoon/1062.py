import sys
from itertools import combinations
sys.stdin = open('input.txt')


N, K = map(int, input().split())
word = [input()[4:-4] for _ in range(N)]    # 단어 앞뒤 알고있는 부분 제거

bin_word = []                               # 각 단어별 필요한 알파벳
need_alpha = set()                          # 모든 단어를 알기 위해 필요한 알파벳
already = 532741                            # 이미 알고 있는 알파벳
answer = 0

for w in word:
    tmp = 0
    for c in w:
        move = (ord(c) - ord('a'))          # 알파벳별 시프트할 숫자
        if not ((1 << move) & already):            # 이미 아는 알파벳이 아니면
            tmp |= 1 << move                # 각 단어의 필요한 알파벳들 2진수로 표현
            need_alpha.add(move)            # 알파벳 시프트한 숫자 저장
            
    bin_word.append(tmp)

K -= 5
if K >= 0:
    if K > len(need_alpha):
        K = len(need_alpha)
    for e in combinations(need_alpha, K):     # 남은 배울수있는 알파벳 갯수로 조합을 구함
        tmp_sum = 0
        tmp_bin = 0
        for a in e:
            tmp_bin |= 1 << a

        for w in bin_word:
            if not (w & ~tmp_bin):
                tmp_sum += 1
        
        if answer < tmp_sum:
            answer = tmp_sum
else:
    answer = 0

print(answer)