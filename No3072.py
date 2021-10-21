counter = 0

b = 0
num = int(input())
while num != 0:
    if num > b:
        b = num
        counter = 1
    elif num == b:
        counter += 1
    num = int(input())

print(counter)
