n = int(input())
a, b = map(int, input().split())
for i in range(n-1):
    new_a = b-a
    b = a
    a = new_a
print(a,b)
