# 15202
# 2022-08-25

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0  # 최대값 초기 설정

    # 십자모양
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            sum10 = L[i][j]
            for k in range(4):  # 4방향
                for p in range(1, P+1):  # 크기
                    ni = i + di[k]*p
                    nj = j + dj[k]*p
                    if 0 <= ni < N and 0 <= nj < N:
                        sum10 += L[ni][nj]
            if maxV < sum10:
                maxV = sum10

    # 대각선모양
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    for i in range(N):
        for j in range(N):
            sumX = L[i][j]
            for k in range(4):  # 4방향
                for p in range(1, P + 1):  # 크기
                    ni = i + di[k] * p
                    nj = j + dj[k] * p
                    if 0 <= ni < N and 0 <= nj < N:
                        sumX += L[ni][nj]
            if maxV < sumX:
                maxV = sumX

    print(f'#{tc} {maxV}')