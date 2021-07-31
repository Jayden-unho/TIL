import sys

testCase = int(sys.stdin.readline().rstrip())

for _ in range(testCase):
    r, string = sys.stdin.readline().split()

    for i in range(len(string)):
        print(string[i]*int(r) ,end="")