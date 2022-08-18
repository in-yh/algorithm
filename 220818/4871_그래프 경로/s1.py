# 4871_그래프 경로
# 2022-08-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V : 노드 개수, E : 간선 개수

    # 간선 정보를 2차원 배열로 만들기
    L = [[] for _ in range(V+1)] # 행수 : 노드 개수+1 -> 인덱스 혼란 방지
    for _ in range(E): # 간선 개수만큼 돌리기
        start, end = map(int, input().split()) # 시작점, 끝점
        L[start].append(end)

    # 출발노드 S, 도착노드 G에 경로 존재하면 1, 존재 안 하면 0
    S, G = map(int, input().split())
    stack = [0]*V
    visited = [0]*(V+1) # 인덱스 혼란 방지
    top = -1
    v = S
    visited[v] = 1
    
    while True:
        for w in L[v]:
            if visited[w] == 0:
                top += 1 # push(v)
                stack[top] = v
                v = w # v <- w
                visited[v] = 1
                break
        else: # 갈 길이 없다면
            if v == G: # 도착노드 G에 도착했다면
                result = 1
                break
            elif top == -1: # stack 비어있다면 출발지로 다시 온 경우(갈 곳이 없었으므로 경로 존재 안하며 break)
                result = 0
                break
            elif top != -1: # stack 비어있지 않다면 pop
                v = stack[top]
                top -= 1

    print('#{} {}'. format(tc, result))