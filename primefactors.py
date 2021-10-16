from math import sqrt
num = int(input())
primes = []


def find_prime(num,j):
    check_prime = False
    for i in range(j,int(sqrt(num))+1):
        print(i, num)
        if num % i == 0:
            check_prime = True
            primes.append(i)
            num = num // i
            find_prime(num,i)
            break
    if check_prime == False:
        primes.append(num)

#find_prime(num,2)
#print(primes)
def find_prime2(num):
    primes = []
    divider = 2
    while divider < int(sqrt(num))+1:
        print(divider,num)
        if num % divider == 0:
            primes.append(divider)
            num = num // divider
        else:
            divider += 1
    primes.append(num)
    return primes

def find_prime3(num):
    primes = {}
    divider = 2
    while divider < int(sqrt(num))+1:
        #print(divider,num)
        if num % divider == 0:
            primes[divider] = primes.get(divider, 0) + 1
            num = num // divider
        else:
            divider += 1
    primes[num] = primes.get(num, 0) + 1
    return primes

print(find_prime3(num))
