
a = 0
b = 0
N = int(input())
while N != 0:
    if N > b:
        b = N
        a = b
    elif N > a:
        a = N

print(a)
