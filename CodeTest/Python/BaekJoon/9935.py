import sys
sys.stdin = open('input.txt')

word = list(sys.stdin.readline().strip())       # 주어진 문자열
bomb = list(sys.stdin.readline().strip())       # 폭발 문자열
answer = []                                     # 정답 스택

B = len(bomb)           # 폭발 문자열의 길이
idx = 0                 # 문자열 인덱스
while idx < len(word):
    answer.append(word[idx])        # 현재 문자열을 스택에 넣음

    if word[idx] == bomb[-1]:       # 현재 문자가 폭발 문자열 마지막 문자와 일치하는 경우
        for k in range(1, B+1):     # 폭발 문자열의 길이만큼 반복
            if len(answer) < B:     # 정답에 쌓인 스택의 길이가 폭발 문자열보다 짧은 경우
                break               # 폭발이 무조건 일어나지 않으므로 종료 (인덱스 에러 방지)

            elif answer[-k] != bomb[-k]:    # 중간에 일치하지 않는 문자가 있으면 종료
                break
        else:                       # 모든 문자가 일치한다면
            for k in range(B):      # 해당하는 문자들 삭제
                answer.pop()
    
    idx += 1

if answer:                          # 남은 문자가 있으면 남은 문자열 출력
    print(''.join(answer))
else:
    print('FRULA')