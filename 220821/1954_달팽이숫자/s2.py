# 1954_달팽이숫자
# 2022-08-21

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [[0]*N for _ in range(N)]

    i = j = 0
    k = 1
    while k <= N*N:
        while j < N and L[i][j] == 0:
            L[i][j] = k
            j += 1
            k += 1
        j -= 1
        i += 1

        while i < N and L[i][j] == 0:
            L[i][j] = k
            i += 1
            k += 1
        i -= 1
        j -= 1

        while j >= 0 and L[i][j] == 0:
            L[i][j] = k
            j -= 1
            k += 1
        j += 1
        i -= 1

        while i >= 0 and L[i][j] == 0:
            L[i][j] = k
            i -= 1
            k += 1
        i += 1
        j += 1

    print('#{}'. format(tc))
    for l in L:
        print(*l)