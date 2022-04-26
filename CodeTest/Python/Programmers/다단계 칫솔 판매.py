import sys
sys.setrecursionlimit(10000)

def solution(enroll, referral, seller, amount):
    enroll_idx = {}                             # 사람 명단이 주어진 순서대로 출력이 필요하므로 '이름': '번호' 형태의 딕셔너리 필요
    result = [0] * len(enroll)                  # 수익금 정답을 저장할 리스트

    def setIdx():                               # 사람들 번호를 지정함
        for i in range(len(enroll)):
            enroll_idx[enroll[i]] = i

    def dfs(name, money):                       # 사람, 수익금
        give = money // 10                      # 부모에게 건내줄 수익금
        mine = money - give                     # 부모에게 수익금 전달하고 남은 금액
        
        idx = enroll_idx.get(name)              # 현재 사람의 번호 가져옴
        result[idx] += mine                     # 현재 사람의 수익금 추가

        if not give: return                     # 부모에게 건내줄 수익금이 없다면 탐색 종료

        next = referral[idx]                    # 부모의 이름
        if next != '-':                         # 최상위 노드가 아니라면 재귀 탐색
            dfs(next, give)

    setIdx()
    for idx in range(len(seller)):              # 수익금 배분 시작
        dfs(seller[idx], amount[idx] * 100)     # 수익을 벌어온 사람, 벌어온 금액
        
    return result

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))