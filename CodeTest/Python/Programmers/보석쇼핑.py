def solution(gems):
    answer = [0, 1e10]
    G = len(set(gems))          # 보석의 종류의 개수
    gems = [''] + gems          # 보석의 번호가 1번부터 시작하므로 인덱스 맞춤

    sign = False                        # 인덱스 범위를 벗어나면 종료
    l, r = len(gems), len(gems)-1       # 두개 포인터의 시작점
    while True:
        buy_gems = set()                # 현재 경우에 구매하는 보석의 종류

        while len(buy_gems) < G:        # 모든 종류 보석을 구매하지 않았다면
            l -= 1                      # 왼쪽 인덱스 감소
            if l <= 0:                  # 왼쪽 인덱스가 범위를 벗어나면 종료
                sign = True
                break
            buy_gems.add(gems[l])       # 왼쪽 인덱스의 보석 추가
        else:
            answer = answer if answer[1]-answer[0] < r-l else [l, r]        # 보석을 종류별로 구매했으면 가장 짧은 거리인지 구분
        
            r = l - 1                                                       # 왼쪽 인덱스를 기준으로하여 오른쪽으로 한번 더 탐색
            buy_gems.clear()                                                # 구매한 보석 종류 리셋

            while len(buy_gems) < G:                                        # 모든 종류 보석을 구매하지 않았으면, 오른쪽 인덱스 증가
                r += 1
                buy_gems.add(gems[r])
            answer = answer if answer[1]-answer[0] < r-l else [l, r]
        
        l = r           # 다음 탐색을 위해, 두개의 포인터는 오른쪽 포인터쪽으로 맞춤
        r = r - 1

        if sign:        # 종료
            break

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))