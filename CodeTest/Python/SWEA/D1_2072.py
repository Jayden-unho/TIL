import sys

testCase = int(sys.stdin.readline().rstrip())

for t in range(1, testCase+1):
    sum = 0
    sum = sum(list(map(lambda x:x if x%2==0 else 0, sys.stdin.readline().rstrip())))

    print(f'#{t} {sum}')