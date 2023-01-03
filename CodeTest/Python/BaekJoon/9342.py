import sys
import re
sys.stdin = open('input.txt')

for _ in range(int(sys.stdin.readline())):
    text = sys.stdin.readline().rstrip()
    pattern = re.compile('^[ABCDEF]?A+F+C+[ABCDEF]?$')

    print('Infected!' if pattern.match(text) else 'Good')
