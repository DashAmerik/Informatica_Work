sx = int(input())
sy = int(input())
ex = int(input())
ey = int(input())

if ex < 1 or ex > 8 or ey <1 or ey > 8:
    print('NO')

else:
    if sx == ex or sy == ey:
        print('YES')

    else:
        print('NO')
#100
