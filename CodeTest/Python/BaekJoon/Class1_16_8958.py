import sys

testCase = int(sys.stdin.readline().rstrip())
score, answer = 0,0

for _ in range(testCase):
    ch = sys.stdin.readline().rstrip()

    for j in range(len(ch)):
        if ch[j] == 'O':
            score += 1
            answer += score
        else:
            score = 0
    print(answer)
    score, answer = 0,0