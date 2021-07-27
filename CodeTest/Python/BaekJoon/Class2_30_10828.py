import sys

def push(x):
    stack.append(x)

def pop():
    if stack == []:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if stack == []:
        print(1)
    else:
        print(0)

def top():
    if stack == []:
        print(-1)
    else:
        print(stack[-1])

number = int(sys.stdin.readline())
stack = []

for _ in range(number):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == 'push': push(cmd[1])
    elif cmd[0] == 'pop': pop()
    elif cmd[0] == 'size': size()
    elif cmd[0] == 'empty': empty()
    elif cmd[0] == 'top': top()