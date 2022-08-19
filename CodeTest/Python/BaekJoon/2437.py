import sys
sys.stdin = open('input.txt')

# 입력데이터
N = int(sys.stdin.readline())
weights = sorted(list(map(int, sys.stdin.readline().split())))

# 불가능한 최소 무게
answer = 1

# 작은 무게의 추부터 시작
for w in weights:
    # 불가능한 최소 무게보다 현재 추가 더 무거우면 종료
    if answer < 1 << w-1:
        break

    # 불가능한 최소 무게 증가
    answer <<= w

print(len(bin(answer))-2)
