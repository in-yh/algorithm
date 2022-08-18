# 2005_파스칼의 삼각형
# 2022-08-17

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    triangle = [[] for _ in range(N)] # triangle N행만큼 만들기

    triangle[0].append(1) # triangle[0][0] = 1
    if N >= 2:
        for i in range(1, N):
            triangle[i].append(1)
            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
            else:
                triangle[i].append(1)
    
    print('#{}'. format(tc))
    for k in range(N):
        print(*triangle[k])