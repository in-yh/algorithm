# 4875_미로
# 2022-08-27

import sys
sys.stdin = open('input.txt', 'r')

def dfs(m, n):
    global answer
    if maze[m][n] == 3:
        answer = 1 # 이 문제에서는 경로 있으면 1 출력(answer += 1이면 경로수 출력)
        return
    else:
        visited[m][n] = 1
        for di, dj in [[0, 1],[1, 0],[0, -1],[-1, 0]]:
            ni, nj = m + di, n + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                dfs(ni, nj)
        visited[m][n] = 0 # 지워줘야 들어올 수 있음!!
        return # 무한루프에 빠지지는 않고 도착하는 경우가 없을 때 return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j

    visited = [[0]*N for _ in range(N)]
    answer = 0
    dfs(sti, stj)
    
    print('#{} {}'. format(tc, answer))