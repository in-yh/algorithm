# 1954_달팽이숫자
# 2022-08-14

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [[0]*N for _ in range(N)]
    k = 1
    L[0][0] = k

    i = 0
    j = 0
    while k < N*N: # N**2을 하던지.. N^2는 아니야.. 
        while j+1 < N and L[i][j+1] == 0: 
            L[i][j+1] = k+1 
            j += 1 
            k += 1 

        while i+1 < N and L[i+1][j] == 0: 
            L[i+1][j] = k+1 
            i += 1 
            k += 1 

        while j-1 >= 0 and L[i][j-1] == 0: 
            L[i][j-1] = k+1
            j -= 1 
            k += 1 

        while i-1 >= 0 and L[i-1][j] == 0: 
            L[i-1][j] = k+1 
            i -= 1 
            k += 1 

    print('#{}'. format(tc))
    for x in L:
        for y in x:
            print(y, end=' ')
        print()