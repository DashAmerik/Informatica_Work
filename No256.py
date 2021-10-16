sx = int(input())
sy = int(input())
ex = int(input())
ey = int(input())

if sx == ex or sy == ey or abs(ey - sy) == abs(ex - sx):
    print('YES')
else:
    print("NO")

#100
