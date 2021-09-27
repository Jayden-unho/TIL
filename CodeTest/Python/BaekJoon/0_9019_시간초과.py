import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(num):
    q = deque([num])

    while q:
        num = q.popleft()

        tmp_1 = D(num)
        tmp_2 = S(num)
        tmp_3 = L(num)
        tmp_4 = R(num)

        for e in [tmp_1, tmp_2, tmp_3, tmp_4]:
            if not result.get(e):
                q.append(e)

                if e == tmp_1:
                    result[e] = [num, 'D']
                elif e == tmp_2:
                    result[e] = [num, 'S']
                elif e == tmp_3:
                    result[e] = [num, 'L']
                elif e == tmp_4:
                    result[e] = [num, 'R']
                
                if e == B:
                    return


def D(num):
    num = (num*2) % 100000
    return num


def S(num):
    num = num - 1
    if not num:
        return 9999
    return num


def L(num):
    n = len(str(num)) - 1
    move = num // (10**n)
    num = (num % (10**n)) * 10
    
    return num + move
    
    # result = 0
    # idx = 1
    # while num >= 10:
    #     result += num%10 * (10**idx)
    #     num //= 10
    #     idx += 1
    # result += num

    # return result


def R(num):
    n = len(str(num)) - 1
    move = (num%10) * (10**n)
    num //= 10

    return num + move

    # tmp = num%10
    # num //= 10
    # result = 0
    # idx = 0
    # while num:
    #     result += num%10 * (10**idx)
    #     num //= 10
    #     idx += 1
    # result += tmp * (10**idx)

    # return result


T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    answer = deque()
    result = {}
    
    bfs(A)
        
    parent = B
    while parent != A:
        answer.appendleft(result[parent][1])
        parent = result[parent][0]
    
    print(''.join(answer))