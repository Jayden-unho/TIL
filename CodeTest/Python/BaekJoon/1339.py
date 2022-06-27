import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                                       # 단어 개수
words = [list(sys.stdin.readline().strip()) for _ in range(N)]      # 단어들
alphabet = {}                                                       # 알파벳이 어느 자리에 몇개가 나오는지 카운트
answer = 0

for word in words:
    mul = len(word) - 1                                     # 자릿수
    for c in word:                                          # 단어의 알파벳 탐색
        alphabet[c] = alphabet.get(c, 0) + 10 ** mul        # 현재 알파벳이 몇 번째 자리수에 한개 있으므로 그 자릿수만큼 더함
        mul -= 1                                            # 다음 아래 자릿수

nums = sorted([v for v in alphabet.values()])               # 값들을 정렬

k = 9                           # 가장 높은 수를 먼저 곱함
while nums:
    answer += nums.pop() * k
    k -= 1

print(answer)

# import sys
# sys.stdin = open('input.txt')

# def solution(n):                    # 알파벳이 사용되는 조합 구하기
#     if n == len(alphabet):          # 모든 알파벳에 치환되는 숫자를 정했을때
#         calc(0, 0)                  # 단어를 숫자로 계산
#         return
    
#     c = ord(alphabet[n]) - 65       # 알파벳 (A->0, Z-> 25)
#     for k in range(10):             # 숫자 0-9
#         if not nums[k]:             # 사용되지 않은 숫자면, 해당 알파벳이 사용
#             nums[k] = 1
#             matching[c] = k
#             solution(n+1)           # 다음 알파벳 탐색
#             nums[k] = 0
#             matching[c] = 0

# def calc(n, ans):                       # 단어를 숫자로 치환하여 계산하는 함수
#     global answer

#     if n == N:
#         answer = max(ans, answer)       # 모두 계산이 되었다면 최대값 저장
#         return
    
#     idx = 0
#     acc = 0
#     while idx < len(words[n]):          # 0의 자리부터 숫자로 변경
#         c = words[n][-idx-1]            # 알파벳
#         num = matching[ord(c) - 65]     # 알파벳을 기록된 숫자로 변경
#         acc += num * (10**idx)          # 숫자의 자리만큼 10을 제곱한 후 더함
#         idx += 1

#     calc(n+1, ans + acc)

# N = int(sys.stdin.readline())                                       # 단어의 개수
# words = [list(sys.stdin.readline().strip()) for _ in range(N)]      # 단어들 목록
# alphabet = set()                                                    # 모든 단어에서 사용되는 알파벳 종류
# matching = [0] * 26                 # 알파벳별 치환되는 숫자
# nums = [0] * 10                     # 숫자의 사용 여부
# answer = 0

# for word in words:                  # 모든 단어를 탐색하여 사용되는 알파벳 정보 확인
#     for c in word:
#         alphabet.add(c)

# alphabet = list(alphabet)           # 집합을 리스트 타입으로 변경
# solution(0)                         # 완전 탐색

# print(answer)