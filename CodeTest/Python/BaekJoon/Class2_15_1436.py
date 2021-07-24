import sys

cnt = int(sys.stdin.readline())

number = 665
while cnt > 0:
    number += 1
    if '666' in str(number):
        cnt -= 1

print(number)