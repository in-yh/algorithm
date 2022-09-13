# 1238_Contact
# 2022-09-13

import sys
sys.stdin = open('input.txt', 'r')

def bfs(n):
    global visited
    q = []
    visited = [0]*101
    q.append(n)
    visited[n] = 1
    while q:
        m = q.pop(0)
        for i in range(1, len(adj[m])): # 인접했고 방문하지 않았다면
            if visited[adj[m][i]] == 0: 
                q.append(adj[m][i])
                visited[adj[m][i]] = visited[m] + 1 # 현재방문횟수 +1


for tc in range(1, 11):
    length, start = map(int, input().split())
    data = list(map(int, input().split()))

    adj = [[0] for _ in range(101)] # 인덱스 i(1~100)와 인접하고 있는 정점 정보
    for i in range(0, length, 2):
        adj[data[i]].append(data[i+1])

    bfs(start) # 방문을 가장 늦게 했던 정점을 구하기 위해(visited가 가장 큰 값 구하기 위해) bfs 이용!

    max_idx = 0
    for idx, value in enumerate(visited):
        if value == max(visited):
            if idx > max_idx:
                max_idx = idx

    print('#{} {}'. format(tc, max_idx))