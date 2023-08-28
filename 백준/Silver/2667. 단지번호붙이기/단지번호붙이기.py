N = int(input())
home = [list(map(int, input())) for _ in range(N)]

# dfs
def dfs(p, q):
    global answer
    for di, dj in [[0, 1],[1, 0],[0, -1],[-1, 0]]:
        ni, nj = p + di, q + dj
        if 0<=ni<N and 0<=nj<N and home[ni][nj]==1 and visited[ni][nj]==0:
            visited[ni][nj] = visited[p][q] + 1
            dfs(ni, nj)
            answer += 1
    # visited[p][q] = 0 # 지워줘야 들어올 수 있음!!
    return

visited = [[0]*N for _ in range(N)]
result = []
for si in range(N):
    for sj in range(N):
        if visited[si][sj]==0 and home[si][sj]==1:
            answer = 1
            visited[si][sj] = 1
            dfs(si, sj)
            result.append(answer)
result.sort()

print(len(result))
for k in range(len(result)):
    print(result[k])