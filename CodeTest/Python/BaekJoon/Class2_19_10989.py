import sys

number = int(sys.stdin.readline())
answer = list([int(sys.stdin.readline())])
tmp_answer = []

while number:
    end_index = len(answer)
    in_num = int(sys.stdin.readline())
    
    for i in range(end_index):
        if answer[i] > in_num:
            tmp_answer = answer.copy()
            answer = list([in_num])
            answer
    number -= 1