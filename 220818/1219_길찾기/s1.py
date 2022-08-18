# 1219_길찾기
# 2022-08-18

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc, road_num = map(int, input().split())
    org_road = list(map(int, input().split()))
    adj_road = [[-1]*100, [-1]*100] # 배열 2개 선언

    # 문제에서 주어진 길 정보(org_road)를 2차원 배열(adj_road)에 넣기
    for j in range(0, len(org_road), 2): # 짝수 인덱스(시작점)만 for문 돌리기
        if adj_road[0][org_road[j]] == -1: # adj_road[0]에 채워져 있지 않다면 인덱스에 시작점을, 값에 도착점을 넣는다. 
            adj_road[0][org_road[j]] = org_road[j+1] 
        else: # adj_road[0]에 이미 채워져 있다면 adj_road[1]에 채운다
            adj_road[1][org_road[j]] = org_road[j+1] 

    # stack, visited 설정
    visited = [0]*100
    stack = [0]*100
    
    # top = -1, s(현위치) = 0(시작점) 및 visited[s] = 1 설정
    top = -1
    s = 0
    visited[s] = 1

    while True:
        for k in range(2): # 2차원 배열의 2개 중 첫 번째부터 순회
            if adj_road[k][s] != -1 and visited[adj_road[k][s]] == 0: # 갈 곳이 있고 방문하지 않았다면
                top += 1 # push(s)!!
                stack[top] = s
                s = adj_road[k][s] # s 위치 옮김
                visited[s] = 1
                break
        else: # 갈 곳이 없다면
            if s == 99: # 99에 도착했으면 result = 1 출력
                result = 1
                break
            elif top == -1: # 도착 못하고 다시 0으로 돌아간다면 result = 0 출력
                result = 0
                break
            else:
                s = stack[top] # pop
                top -= 1

    print('#{} {}'. format(tc, result))