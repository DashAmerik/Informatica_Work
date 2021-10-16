sx = int(input())
sy = int(input())
ex = int(input())
ey = int(input())


if (abs(sx - ex) == 2 and abs(sy - ey) == 1) or (abs(sy - ey) == 2 and abs(sx - ex) == 1):
    print("YES")
else:
    print("NO")
