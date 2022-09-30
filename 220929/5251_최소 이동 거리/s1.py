# 5251_최소 이동 거리
# 2022-09-29

import sys
sys.stdin = open('input.txt', 'r')

def dijkstra(N, x):
    U = [x] # 방문한 정점 체크
    for i in range(N+2): # 모든 정점 순회하며 d 채우기
        d[i] = adjM[x][i]
    
    for _ in range(1, N+1): # (N+1)개의 정점 중 출발을 제외한 정점 선택(while 대신)
        w = N+1
        for i in range(N+1): # U에 포함되지 않은 d가 최소인 정점 w 선택
            if (i not in U) and d[i] < d[w]:
                w = i
        U.append(w) # U에 w 넣기
        for v in range(N+1): # 정점 v가
            if 0<adjM[w][v]<11*1000000: # w에 인접이면
                d[v] = min(d[v], d[w]+adjM[w][v])
    return d[v]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split()) # N 마지막 노드 번호
    adjM = [[11*1000000]*(N+2) for _ in range(N+2)] # 가장 큰 인접행렬 만들어주기
    for i in range(N+2): # 자기자신에서 자기자신으로 가는 간선 가중치는 없기 때문에 0으로 만들어주기
        adjM[i][i] = 0
    for _ in range(E): # 연결되어 있는 것은 인접행렬에 표시해주기
        s, e, w = map(int, input().split())
        adjM[s][e] = w
    d = [11*1000000]*(N+2) # 거리 리스트
    print('#{} {}'.format(tc, dijkstra(N, 0)))