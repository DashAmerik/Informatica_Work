k = list(map(int,input().split()))
i_element, element = map(int,input().split())
k.append(0)
for i in range(len(k)-1,i_element, -1):
    k[i] = k[i-1]
k[i_element] = element
print(*k)
