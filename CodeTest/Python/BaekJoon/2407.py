n, m = map(int, input().split())

factorial = [0] * (n+1)
factorial[1] = 1

for idx in range(2, n+1):
    factorial[idx] = factorial[idx-1] * idx

print(factorial[n] // (factorial[m]*factorial[n-m]))