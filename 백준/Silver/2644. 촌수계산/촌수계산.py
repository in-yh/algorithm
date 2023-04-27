family_num = int(input())
ans_i, ans_j = map(int, input().split())

adj = [[0]*(family_num+1) for _ in range(family_num+1)]

relation_num = int(input())
for _ in range(relation_num):
    p, c = map(int, input().split())
    adj[p][c] = 1
    adj[c][p] = 1

stack = []
visited = [0]*(family_num+1)
stack.append(ans_i)
visited[ans_i] = 1
while stack:
    u = stack.pop(0)
    if u == ans_j:
        break
    for v in range(1, family_num+1):
        if adj[u][v]==1 and visited[v]==0: # 관계가 있으면
            stack.append(v)
            visited[v] = visited[u] + 1

if visited[ans_j] == 0:
    print(-1)
else:
    print(visited[ans_j]-1)
