# 9489_고대 유적
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N):
        cnt = 0 # 여기에 초기화!! i가 바뀔 때마다 초기화 해야함!!
        for j in range(M):
            if L[i][j] == 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0

    for k in range(M):
        cnt = 0
        for l in range(N):
            if L[l][k] == 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    
    print('#{} {}'. format(tc, max_cnt))