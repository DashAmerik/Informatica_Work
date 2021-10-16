sx = int(input())
sy = int(input())
ex = int(input())
ey = int(input())

if abs(ey - sy) == 1 or abs(ex - sx) == 1:
    print("YES")
else:
    print("NO")
