import sys
from collections import deque
sys.stdin = open('input.txt')

S = int(sys.stdin.readline())                   # 목표 이모티콘 길이
visited = {}                                    # 이모티콘, 클립보드 길이별 탐색 여부

q = deque([(1, 0, 0)])                          # 초기 이모티콘 길이 1, 클립보드 0, 연산 시간 0

while q:
    emoticon, clipboard, ans = q.popleft()      # 현재 이모티콘 길이, 클립보드 길이, 연산 시간
    if emoticon == S:                           # 이모티콘 길이가 목표 도달시, 종료
        print(ans)
        break
    elif emoticon <= 0:                         # 이모티콘의 길이 음수가 되려는 경우, 해당 경우 무시
        continue

    ans += 1                                                        # 연산 시간 + 1

    if not visited.get((emoticon, emoticon), False):                # 클립보드에 복사한 경우
        visited[(emoticon, emoticon)] = ans                         # 방문 처리
        q.append((emoticon, emoticon, ans))                         # 큐에 추가

    if not visited.get((emoticon+clipboard, clipboard), False):     # 이모티콘에 붙여넣기 한 경우
        visited[(emoticon+clipboard, clipboard)] = ans
        q.append((emoticon+clipboard, clipboard, ans))
    
    if not visited.get((emoticon-1, clipboard), False):             # 이모티콘 하나 삭제한 경우
        visited[(emoticon-1, clipboard)] = ans
        q.append((emoticon-1, clipboard, ans))