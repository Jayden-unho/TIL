import sys

year = int(sys.stdin.readline().rstrip())
sign = 0

if(year%4 == 0 and year%100 != 0 or year%400 == 0):
    sign = 1

print(sign)