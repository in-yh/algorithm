N, M, V = map(int, input().split())

visited = [0]*(N+1)
adj = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

# dfs
def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for i in range(N+1):
        if visited[i] == 0 and adj[v][i] == 1:
            dfs(i)

visited = [0]*(N+1)
dfs(V)
print()

# bfs
visited2 = [0]*(N+1)
stack2 = []
stack2.append(V)
visited2[V] = 1
while stack2:
    a = stack2.pop(0)
    print(a, end=" ")
    for i in range(N+1):
        if adj[a][i] == 1 and visited2[i] == 0:
            stack2.append(i)
            visited2[i] = 1