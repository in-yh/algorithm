# 5249_최소 신장 트리
# 2022-09-29

import sys
sys.stdin = open('input.txt', 'r')

# kruskal
def find_set(x): # 대표원소 찾는 함수
    while x != rep[x]: # 같을 때까지 찾아주기
        x = rep[x]
    return x

def union(x, y): # 합쳐서 x를 대표원소로 하는 함수
    rep[find_set(y)] = find_set(x)
    return

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V : 마지막 노드 번호 / V+1 : 노드 개수
    edge = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append([u, v, w])
    edge.sort(key=lambda x:x[2]) # 간선 가중치 작은 순서대로 sort
    rep = [i for i in range(V+1)]

    total = 0
    cnt = 0
    for u, v, w in edge: # 가중치가 작은 것부터 순회하면서
        if find_set(u) != find_set(v): # u와 v가 연결되어 있지 않다면(u의 대표원소와 v의 대표원소가 다르다면)
            union(u, v) # 연결해주고(합쳐서 u를 대표원소로 만든다)
            total += w # 간선 더해주고
            cnt += 1 # 횟수 1증가
           
            if cnt == V: # 횟수가 간선수만큼 돌았다면 break
                break
    
    print('#{} {}'.format(tc, total))