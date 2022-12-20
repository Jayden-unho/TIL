import sys
sys.stdin = open('input.txt')

palindrome = sys.stdin.readline().rstrip()
N = len(palindrome)

if palindrome == palindrome[::-1]:
    if palindrome == palindrome[0] * N:
        print(-1)
    else:
        print(N-1)
else:
    print(N)
