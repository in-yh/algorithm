# 4861_회문
# 2022-08-16

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 20 13
    L = [list(map(str, input())) for _ in range(N)]

    # 행
    for i in range(N): # 0~19
        for j in range(N-M+1): # 0~7
            cnt = 0
            for k in range(M//2): # 0~5
                if L[i][j + k] == L[i][j+(M-1) - k]: # [0]=[12] -> [j]=[j+(M-1)]
                    cnt += 1 # 맞을 때마다 cnt + 1
                if cnt == M//2: # 6
                    result_list = L[i][j:j+M] # L[i][0:13]
                    result = ''.join(result_list) # TLMMHOOOHMMLT               

    # 열
    for i in range(N): # 0~9
        for j in range(N-M+1): # 0
            cnt = 0
            for k in range(M//2): # 0~4
                if L[j + k][i] == L[j+(M-1) - k][i]: # [0 + 1][2] == [0+9 - 1][2]
                    cnt += 1 # 맞을 때마다 cnt + 1
                if cnt == M//2: # 5
                    result_list = [] 
                    for l in range(j, j+M): # L[j:j+M][i] 안 됨
                        result_list.append(L[l][i])
                    result = ''.join(result_list)

    print('#{} {}'. format(tc, result))