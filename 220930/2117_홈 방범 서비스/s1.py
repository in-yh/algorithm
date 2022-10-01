# 2117_홈 방범 서비스
# 2022-09-30

import sys
sys.stdin = open('input.txt', 'r')

def bfs(sti, stj, k, N):
    global cnt
    q = []
    visited = [[0]*N for _ in range(N)]
    q.append((sti, stj))
    visited[sti][stj] = 1
    
    while q:
        i, j = q.pop(0)

        if abs(i-sti) + abs(j-stj) == k:
            return

        if home[i][j] == 1:
            cnt += 1

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    home = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    for i in range(N):
        for j in range(N):
            for k in range(1, N+2): # 가운데 기준으로 N+1까지 돌리면 됨
                cnt = 0
                bfs(i, j, k, N)
                if cnt*M - (k*k+(k-1)*(k-1)) >= 0:
                    if result < cnt:
                        result = cnt

    print('#{} {}'.format(tc, result))