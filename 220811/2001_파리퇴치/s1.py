# 2001_파리퇴치
# 2022-08-11

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for k in range(M):
                for l in range(M):
                    s += L[i+k][j+l]
            if maxV < s:
                maxV = s
    
    print('#{} {}'. format(tc, maxV))