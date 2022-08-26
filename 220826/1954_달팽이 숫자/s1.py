# 1954_달팽이 숫자
# 2022-08-26

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [[0]*N for _ in range(N)]
    
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    L[0][0] = 1 
    number = 2
    i = j = 0
    k = 0
    while number <= N*N:
        # 오른쪽으로 가다가 벽이 아니고 0 아니면 k 할당  
        ni, nj = i + di[k%4], j + dj[k%4] 
        if 0<=ni<N and 0<=nj<N and L[ni][nj] == 0:
            L[ni][nj] = number
            i, j = ni, nj
            number += 1
        # 오른쪽으로 가다가 벽을 만나거나 0이 아닌 숫자를 만나면 방향 전환
        else:
            k += 1
    
    print('#{}'. format(tc))
    for x in range(N):
        print(*L[x])