k = list(map(int,input().split()))
i_element = int(input())
for i in range(i_element,len(k)-1):
    k[i] = k[i+1]
k.pop()
print(*k)
