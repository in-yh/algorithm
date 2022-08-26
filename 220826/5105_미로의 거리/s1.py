# 5105_미로의 거리
# 2022-08-26

import sys
sys.stdin = open('input.txt', 'r')

def bfs(m, n, num):
    visit = [[0]*num for _ in range(num)] # visit 생성
    q = [] # 큐 생성
    q.append((m, n)) # 시작점 인큐
    visit[m][n] = 1
    while q:
        m, n = q.pop(0) # 디큐
        if maze[m][n] == 3: # 해야할 일
            return visit[m][n]-2
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 인접하면서 방문하지 않은 점 인큐
            ni = m + di
            nj = n + dj
            if 0<=ni<num and 0<=nj<num and maze[ni][nj]!=1 and visit[ni][nj]==0:
                q.append((ni, nj))
                visit[ni][nj] = visit[m][n] + 1
    return 0 # 다 돌았는데도 없으면 0 출력!!

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
    
    print('#{} {}'. format(tc, bfs(sti, stj, N)))