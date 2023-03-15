import sys
from itertools import permutations
sys.stdin = open("input.txt")


N = int(sys.stdin.readline())
nums = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
cnts = [0] * 3
answer = 1e10

# 각 모양이 몇 개씩 존재하는지 카운트
for i in range(3):
    cnts[i] = nums.count(i)

# 같은 모양끼리 정돈되는 결과들 (6가지 경우)
for permu in permutations(enumerate(cnts), 3):
    ans = 0  # 현재 경우 정답
    idx = 0  # 영역을 구분하기 위한 인덱스

    first = permu[0][0]  # 1번 영역의 도형 타입
    second_third = []    # 2, 3번 영역이 서로 교환이 필요한 개수 저장할 변수
    for t, cnt in permu:
        part = nums[idx:idx+cnt]

        for i in range(3):
            # 도형이 원래 있어야하는 자리에 있으면 움직일 필요 없음
            if i == t:
                continue

            # 1번 영역인 경우 2, 3번 영역으로 이동해야하는 개수 추가
            if first == t:
                ans += part.count(i)
            # 2, 3번째 영역인 경우 서로 교환해야하는 개수 카운트해서 배열에 추가
            elif first != t and i != first:
                second_third.append(part.count(i))
        idx += cnt

    ans += max(second_third)   # 2, 3번째 서로 교환해야하는 개수 중 큰 값을 더하기
    answer = min(answer, ans)  # 최소 정답 구하기

print(answer)
