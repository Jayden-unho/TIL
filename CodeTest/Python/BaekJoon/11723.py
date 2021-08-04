import sys

m = int(sys.stdin.readline())
s = set()

def add(x):
    if x not in s:
        s.add(x)

def remove(x):
    if x in s:
        s.remove(x)

def check(x):
    if x in s:
        print(1)
    else:
        print(0)

def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)

def all():
    s.update([i for i in range(1,21)])

def empty():
    s.clear()

for _ in range(m):
    command = list(sys.stdin.readline().split())

    if command[0] == 'add':
        add(int(command[1]))
    elif command[0] == 'remove':
        remove(int(command[1]))
    elif command[0] == 'check':
        check(int(command[1]))
    elif command[0] == 'toggle':
        toggle(int(command[1]))
    elif command[0] == 'all':
        all()
    elif command[0] == 'empty':
        empty()