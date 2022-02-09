import sys
sys.stdin = open('input.txt')


def make_table(pattern):
    j = 0                                       # 접두사 인덱스
    for i in range(1, len(pattern)):            
        if j > 0 and pattern[i] != pattern[j]:  # 접두사 인덱스와 가장 마지막 문자가 일치하지 않으면, 접두사 인덱스 초기화
            j = 0

        if pattern[i] == pattern[j]:            # 현재 접두사 인덱스와 가장 마지막 인덱스의 문자가 일치하면
            j += 1                              # 접두사 인덱스 증가
            table[i] = j                        # 테이블에 접두사 인덱스 값 저장

def solution(s, pattern):                       # KMP 탐색
    make_table(pattern)                         # 접두사 접미사 일치하는 일덱스 찾기 위한 테이블 생성
    j = 0                                       # 찾으려는 문자열(패턴)의 인덱스
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:     # 문자가 일치하지 않으면
            j = table[j - 1]                    # 테이블에 기록한 패턴의 인덱스로 수정

        if s[i] == pattern[j]:                  # 문자가 일치하면
            if j == len(pattern) - 1:           # 패턴과 일치하는 문자열을 찾았으면 종료
                return True
            else:                               # 아직 전부 탐색이 아니라면, 패턴의 다음 자릿수 탐색 위한 인덱스 증가
                j += 1
    return False

s = sys.stdin.readline().strip()            # 전체 문자열
pattern = sys.stdin.readline().strip()      # 찾으려는 문자열
table = [0] * len(pattern)                  # 문자열 접두사 접미사 일치하는 개수 확인 리스트

if solution(s, pattern):                    # 탐색
    print('1')
else:
    print('0')