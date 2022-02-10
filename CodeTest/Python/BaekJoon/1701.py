import sys
sys.stdin = open('input.txt')

def make_table(pattern):
    global answer

    table = [0] * len(pattern)

    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        
        if pattern[i] == pattern[j]:
            j += 1            
            table[i] = j
    
    answer = max(answer, max(table))

s = sys.stdin.readline().rstrip()
answer = 0

i = 0
while i < len(s) - answer:
    make_table(s[i:])
    i += 1

print(answer)