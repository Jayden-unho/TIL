def solution(n, build_frame):
    built = set()

    def is_right(): 
        for b in built:                     # 모든 구조물 탐색
            x, y, a = b                     # x, y 좌표, a-0: 기둥, 1: 보
            
            if not a:                       # 현재 구조물이 기둥이라면
                if y and (x, y-1, 0) not in built and ((x, y, 1) not in built and (x-1, y, 1) not in built):                                # 조건에 해당하지 않으면
                    return False
            else:                           # 현재 구조물이 보라면
                if ((x, y-1, 0) not in built and (x+1, y-1, 0) not in built) and ((x-1, y, 1) not in built or (x+1, y, 1) not in built):    # 조건에 해당하지 않으면
                    return False
        return True                         # 모든 조건에 충족할 경우 True 반환

    for info in build_frame:
        x, y, a, b = info                   # x, y 좌표, a-0: 기둥, 1: 보, b-0:삭제, 1: 설치
        
        if not b:                           # 삭제한다면
            built.remove((x, y, a))         # 삭제 실행
            if not is_right():              # 조건에 충족하지 않으면, 다시 설치
                built.add((x, y, a))
        else:                               # 설치한다면
            built.add((x, y, a))            # 설치 실행
            if not is_right():              # 조건에 충족하지 않으면, 다시 제거
                built.remove((x, y, a))

    return sorted(built)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))