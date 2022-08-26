# 12712_파리퇴치3
# 2022-08-26

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    # 십자모양
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            sum_10 = L[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i + di[k]*m
                    nj = j + dj[k]*m
                    if 0<=ni<N and 0<=nj<N:
                        sum_10 += L[ni][nj]
            if sum_10 > maxV:
                maxV = sum_10
                            
    # 대각선모양
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    for i in range(N):
        for j in range(N):
            sum_X = L[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i + di[k]*m
                    nj = j + dj[k]*m
                    if 0<=ni<N and 0<=nj<N:
                        sum_X += L[ni][nj]
            if sum_X > maxV:
                maxV = sum_X

    print('#{} {}'. format(tc, maxV))