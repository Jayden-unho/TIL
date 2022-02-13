def solution(key, lock):
    K, L = len(key), len(lock)                                  # 키와 자물쇠의 한변의 길이

    keys = [[[0] * K for _ in range(K)] for _ in range(4)]      # 회전한 키의 모양들을 담을 리스트

    for i in range(K):
        for j in range(K):
            keys[0][i][j] = key[i][j]               # 정방향
            keys[1][i][j] = key[K-1-j][i]           # 90도 회전
            keys[2][i][j] = key[K-1-i][K-1-j]       # 180도 회전
            keys[3][i][j] = key[j][K-1-i]           # 270도 회전

    def can_open(y, x):                                         # 자물쇠를 열 수 있는지 확인하는 함수
        r, c = y, x                                             # 키 정보가 담긴 배열의 행과 열
        for i in range(L):                                      # 자물쇠의 크기만큼 반복
            for j in range(L):
                if 0 <= r < K and 0 <= c < K:                   # 키의 인덱스가 배열 내의 범위라면
                    if lock[i][j] and keys[t][r][c]:            # 자물쇠와 키가 돌기라면, False 반환
                        return False
                    elif not lock[i][j] and not keys[t][r][c]:  # 자물쇠와 키가 홈이라면, False 반환
                        return False
                elif not lock[i][j]:                            # 자물쇠가 홈이라면, False 반환
                    return False
                c += 1                                          # 열 인덱스 증가
            c = x                                               # 새로운 행이므로 열 초기값으로 다시 할당 및 행 증가
            r += 1
        return True                                             # 자물쇠를 열 수 있다면, True 반환

    for y in range(-L, K):              # 키가 오른쪽 아래부터 시작
        for x in range(-L, K):
            for t in range(4):          # 회전한 4개의 키를 모두 확인해야함
                if can_open(y, x):      # 자물쇠를 열 수 있다면 True 반환하며 종료
                    return True

    return False                        # 자물쇠를 열 수 없다면 False 반환

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))