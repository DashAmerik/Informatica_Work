L = int(input())
k = list(map(int,input().split()))

for i in range(L//2)):
    k[i], k[L - i - 1] = k[L - i - 1], k[i]

print(*k)
