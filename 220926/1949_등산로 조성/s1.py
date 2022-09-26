# 1949_등산로 조성
# 2022-09-25

import sys
sys.stdin = open('input.txt', 'r')

def DFS(i, j, cnt, result):
    global max_result
    if max_result < result:
        max_result = result

    visited[i][j] = 1
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
            if cnt == 0 and road[i][j] - road[ni][nj]<=0:
                for k in range(1, K+1):
                    road[ni][nj] = road[ni][nj]-k
                    if road[i][j]-road[ni][nj]>0:
                        DFS(ni, nj, 1, result+1)
                    road[ni][nj] = road[ni][nj]+k
            elif road[i][j]-road[ni][nj]>0:
                DFS(ni, nj, cnt, result+1)
            visited[ni][nj] = 0 # 원상복구.. 여기서!


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(N):
            if maxV < road[i][j]:
                maxV = road[i][j]

    start = [] # 초기좌표 구해주는 거 이 방법으로!
    for i in range(N):
        for j in range(N):
            if road[i][j] == maxV:
                start.append((i, j))
    
    max_result = 0
    for sti, stj in start:
        visited = [[0]*N for _ in range(N)]
        DFS(sti, stj, 0, 1)
    print('#{} {}'.format(tc, max_result))            