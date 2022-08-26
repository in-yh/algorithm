# 9489_고대유적
# 2022-08-26

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    # 행 검사
    for i in range(N):
        cnt = 0
        j = 0
        while j < M:
            if L[i][j] == 1:
                while j < M and L[i][j] == 1:
                    cnt += 1
                    j += 1
                if cnt > maxV:
                    maxV = cnt
                cnt = 0
            else:
                j += 1

    # 열 검사
    for l in range(M):
        cnt = 0
        k = 0
        while k < N:
            if L[k][l] == 1:
                while k < N and L[k][l] == 1:
                    cnt += 1
                    k += 1
                if cnt > maxV:
                    maxV = cnt
                cnt = 0
            else:
                k += 1
    
    print('#{} {}'. format(tc, maxV))