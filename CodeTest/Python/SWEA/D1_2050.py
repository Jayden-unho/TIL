input_string = input().rstrip()
li = []

for c in input_string:
    num = ord(c) - 64
    li.append(str(num))

print(" ".join(li))