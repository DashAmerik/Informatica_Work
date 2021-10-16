N = int(input())
L = input()
newN = N

def check_len(N, L):
    #print('enter check', N)
    i = (N + 1) // 2
    #print('init i', i)
    while i < len(L):
        #print('check pair', i, N - i - 1)
        if L[i] != L[N-i-1]:
            return False
        i += 1
    return True

def find_len(N, L):
    for i in range(N, 2 * N):
        if check_len(i, L):
            return i

palindrome_len = find_len(N, L)
print(palindrome_len)



'''
1 2 3 2 L
4 N
0 - 3
1 - 2
5 N
0-4
1-3



1 2 3 4 3 2 1
0 1 2 3 4 5 6

0 - 6
1 - 5
2 - 4


0-4
1-3

23565

0-4
1-3
i  -  n-1
0-5
1-4
2-3

0-6
1-5
2-4


0-7
1-6
2-5
3-4
4 - 2
5 - 3
6 - 3
7 - 4
8 - 4
'''
