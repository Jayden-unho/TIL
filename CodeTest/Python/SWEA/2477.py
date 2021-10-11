import sys
sys.stdin = open('input.txt')


T = int(input())
answer = []

for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())       # 접수 창구 개수 / 정비 창구 개수 / 고객 수 / 지갑 두고간 고객 (접수 창구 번호 / 정비 창구 번호)
    reception = list(map(int, input().split()))     # 고장 접수 시간 N개
    repair = list(map(int, input().split()))        # 차량 정비 시간 M개
    K = int(input())                                # 고객 방문 시간
    elapse = 0                                      # 흐른 시간
    idx_reception, idx_repair = 0, 0                # 접수 인덱스 / 정비 인덱스 (어느 사람 차례인지)

    task_reception, task_repair = [0] * N, [0] * M      # 일하는 중인 접수/정비 상황

    while idx_repair < M:       # 정비 모두 끝날때 까지
        elapse += 1

        