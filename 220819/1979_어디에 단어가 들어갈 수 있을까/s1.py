# 1979_어디에 단어가 들어갈 수 있을까
# 2022-08-19

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N-K+1):
            if 0 < j < N-K:
                if L[i][j-1] != 1 and L[i][j:j+K] == [1]*K and L[i][j+K] != 1: # [1]*K 해야함.. 리스트 개수에 맞게
                    result += 1
            elif j == 0:
                if L[i][j:j+K] == [1]*K and L[i][j+K] != 1:
                    result += 1
            elif j == N-K:
                if L[i][j-1] != 1 and L[i][j:j+K] == [1]*K:
                    result += 1
                
    for k in range(N):
        for l in range(N-K+1):
            if 0 < l < N-K and L[l-1][k] != 1 and L[l+K][k] != 1:
                cnt = 0
                for a in range(l, l+K):
                    if L[a][k] == 1:
                        cnt += 1
                if cnt == K:
                    result += 1
            elif l == 0 and L[l+K][k] != 1:
                cnt = 0
                for b in range(l, l+K):
                    if L[b][k] == 1:
                        cnt += 1
                if cnt == K:
                    result += 1
            elif l == N-K and L[l-1][k] != 1:
                cnt = 0
                for c in range(l, l+K):
                    if L[c][k] == 1:
                        cnt += 1
                if cnt == K:
                    result += 1
                        
    print('#{} {}'. format(tc, result))