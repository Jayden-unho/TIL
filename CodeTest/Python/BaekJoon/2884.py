h, m = input().split()
h = int(h)
m = int(m)

a = 60*h + m
b = a - 45

if b>=0:
    h = b//60
    m = b - h*60
else:
    h = 23
    m = 60 + b
print(h, m)