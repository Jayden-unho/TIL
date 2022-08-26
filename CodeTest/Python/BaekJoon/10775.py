import sys
sys.setrecursionlimit(100000000)
sys.stdin = open('input.txt')


def union(a: int) -> int:
    '''
    게이트에 비행기 도킹

        params:
            a: 도킹 시도하려는 게이트 번호
        returns:
            a: 도킹한 게이트 번호
    '''
    a = find(a)
    li[a] = a - 1
    return a


def find(a: int) -> int:
    '''
    해당 게이트보다 작은 게이트에서 도킹이 가능한 게이트를 찾기 위해 탐색
    도킹이 가능한 게이트 번호 반환

        params:
            a: 도킹 가능 여부 확인이 필요한 게이트 번호
        returns:
            a: 도킹 가능한 게이트 번호
    '''
    if li[a] != a and a >= 0:
        li[a] = find(li[a])
        return li[a]
    return a


def solution() -> int:
    '''
    비행기가 들어오는 순서에 따라 도킹 시뮬레이션

        returns:
            ans: 도킹 가능한 최대 비행기 수
    '''
    ans = 0

    for _ in range(P):
        num = int(sys.stdin.readline())

        if union(num-1) == -1:  # 도킹한 게이트 번호가 -1이면, 불가능한 게이트이므로 종료
            break
        else:                   # 도킹 성공시 정답 1 증가
            ans += 1

    return ans


# 입력 값
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

# 도킹할 게이트들 목록
li = list(range(G))

print(solution())
