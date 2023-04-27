N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
stack = []
stack.append((0, 0))
visited[0][0] = 1
while stack:
    i, j = stack.pop(0)
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0 and maze[ni][nj]==1:
            stack.append((ni,nj))
            visited[ni][nj] = visited[i][j] + 1

print(visited[N-1][M-1])