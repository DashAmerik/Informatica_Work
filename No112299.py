L = int(input())
k = list(map(int,input().split()))
l_bound, h_bound = map(int,input().split())
l_bound -= 1
h_bound -= 1
sum = (l_bound + h_bound)
for i in range(l_bound, sum // 2)):
    k[i], k[sum - i - 1] = k[sum - i - 1], k[i]
print(*k)
