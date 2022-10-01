# 1249_보급로
# 2022-09-30

import sys
sys.stdin = open('input.txt', 'r')

def work(i, j, N):
    global result 
    q = []
    result = [[10*100*100]*N for _ in range(N)]
    q.append((i, j))
    result[i][j] = 0
    while q:
        i, j = q.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                if result[ni][nj] > result[i][j] + maps[ni][nj]: # 최소값으로 갱신되면 그쪽으로 가봐야 하니깐 q에 append도 해주고 갱신되지 않으면 갈 필요도 없으므로 append 해주지 않는다.
                    result[ni][nj] = result[i][j] + maps[ni][nj]
                    q.append((ni, nj))
        

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]

    work(0, 0, N)
    print('#{} {}'.format(tc, result[N-1][N-1]))