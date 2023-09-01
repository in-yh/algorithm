M,N,K = map(int, input().split())
zone = [[0]*N for _ in range(M)] 


def bfs(si, sj, a):
    global area
    visited[si][sj] = a
    stack.append((si, sj))
    while stack:
        p, q = stack.pop(0)
        for dp, dq in [[0,1],[1,0],[0,-1],[-1,0]]:
            np, nq = p+dp, q+dq
            if 0<=np<M and 0<=nq<N and zone[np][nq]==0 and visited[np][nq]==0:
                visited[np][nq] = visited[p][q]
                area += 1
                stack.append((np, nq))
    return area


for _ in range(K):
    sx, sy, fx, fy = map(int, input().split())
    for y in range(sy, fy):
        for x in range(sx, fx):
            zone[y][x] = 1

visited = [[0]*N for _ in range(M)] 
stack = []
a = 1 
result = []
for i in range(M):
    for j in range(N):
        if zone[i][j]==0 and visited[i][j]==0:
            area = 1
            result.append(bfs(i, j, a)) 
            a += 1

result.sort()

print(a-1)
print(*result)