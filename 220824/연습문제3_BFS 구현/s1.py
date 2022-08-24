# 연습문제3_BFS 구현
# 2022-08-24

import sys
sys.stdin = open('input.txt', 'r')

def bfs(v, N): # v 시작정점, N 정점개수
    visited = [0] * (N+1) # visited 생성, 인덱스 혼란 방지
    q = [] # 큐 생성
    q.append(v) # 시작정점 인큐 및 방문 처리
    visited[v] = 1
    while q: # 큐가 비어있지 않다면
        v = q.pop(0) # 디큐
        result.append(v)
        for w in adjList[v]: # 인접한 곳이 방문하지 않았다면 인큐 및 방문처리
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

fixes, lines = map(int, input().split())
L = list(map(int, input().split()))
adjList = [[] for _ in range(fixes+1)] # 8줄, 인덱스 혼란 방지

for i in range(len(L)):
    if i%2 == 0: # 짝수인덱스면
        adjList[L[i]].append(L[i+1]) # 양방향
        adjList[L[i+1]].append(L[i])
# adjList : [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]] ?

# 출력하기
result = []
bfs(1, fixes)
for j in range(fixes-1):
    print(result[j], end='-')
print(result[fixes-1])