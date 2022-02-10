import sys
sys.stdin = open('input.txt')

def make_table(pattern):                            # KMP에서 이용되는 접두사와 접미사가 일치하는 길이를 저장하는 테이블 구하기
    global answer

    table = [0] * len(pattern)                      # 테이블 초기화

    j = 0                                           # 접두사 인덱스
    for i in range(1, len(pattern)):                
        while j > 0 and pattern[i] != pattern[j]:   # 접두사 인덱스의 문자와 가장 마지막 문자가 일치하지 않으면
            j = table[j-1]                          # 테이블에 저장된 인데스로 값 변경
        
        if pattern[i] == pattern[j]:                # 문자가 일치하면
            j += 1                                  # 접두사 인덱스 증가
            table[i] = j                            # 일치하는 길이 저장
    
    answer = max(answer, max(table))

s = sys.stdin.readline().rstrip()   # 입력 받은 문자열
answer = 0                          # 정답 변수

i = 0                               # 가장 앞에서부터 시작
while i < len(s) - (answer*2):      # 확인할 문자가 정답의 길이보다 짧다면 확인할 필요가 없음
    make_table(s[i:])               # KMP 알고리즘에서 사용하는 접두사 접미사가 일치하는 길이 저장하는 테이블 구함
    i += 1

print(answer)