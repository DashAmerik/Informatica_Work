from collections import Counter


def counter(w1):
    d1 = {}
    for c in w1:
        if not (c in d1):
            d1[c] = 0
        d1[c] += 1
    return d1

def is_anagram(w1, w2):
    if not(len(w1) == len(w2)):
        return False

    d1 = counter(w1)
    d2 = counter(w2)

    for key in d1:
        if not(key in d2):
            return False
        elif not(d1[key] == d2[key]):
            return False
    return True


w1 = input()
w2 = input()

ans = is_anagram(w1, w2)
if ans == True:
    print("YES")
else:
    print("NO")


#list[<start>:<stop>:<step>]
