n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

def bfs(i, j):
    global cnt
    visited[i][j]=1
    stack.append((i, j))
    while stack:
        i, j = stack.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m and picture[ni][nj]==1 and visited[ni][nj]==0:
                visited[ni][nj] = 1
                stack.append((ni, nj))
                cnt += 1

visited = [[0]*m for _ in range(n)]
stack = []
area_cnt = 0
answer = 0
for i in range(n):
    for j in range(m):
        if picture[i][j]==1 and visited[i][j]==0:
            cnt = 1
            bfs(i, j)
            area_cnt += 1
            answer = max(answer, cnt)

print(area_cnt)
print(answer)