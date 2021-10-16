A = int(input())
B = int(input())
C = int(input())



def bigger(A, B, C):
    if A >= B and A >= C:
        return A

    if B >= A and B >= C:
        return B

    if C >= B and C >= A:
        return C
print(bigger(A,B,C))

#100
