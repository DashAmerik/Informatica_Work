num = int(input())
from math import sqrt

def find_factors(num):
    factors = []
    divider = 1
    for i in range(int(sqrt(num))+1):
        if num % divider == 0:
            factors.append(divider)
            factors.append(num//divider)
        divider += 1
    return factors

print(find_factors(num))
