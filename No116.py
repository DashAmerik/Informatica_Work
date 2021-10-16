N = int(input())
big = 0
small = 10
while N != 0:
    a = N%10
    if a > big:
        big = a
    if a < small:
        small = a
    N = N//10
print(big, small)
