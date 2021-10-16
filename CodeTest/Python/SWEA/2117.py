"""
최소한 이득을 봐야함 - 모든 
"""


import sys
sys.stdin = open('input.txt')


T = int(input())
answer = []

for tc in range(1, T+1):
    N, M = map(int, input().split())        # length of array / cost each home
    village = [list(map(int, input().split())) for _ in range(N)]

