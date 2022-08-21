# 2005_파스칼의 삼각형
# 2022-08-21

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [['']*N for _ in range(N)] # 공백으로 만들기

    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i: # i 기준으로 안 나눠도 돼
                L[i][j] = 1
            else:
                L[i][j] = L[i-1][j-1] + L[i-1][j]
    
    print('#{}'. format(tc))
    for k in range(N):
        print(*L[k])