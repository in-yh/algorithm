# 1861_정사각형 방
# 2022-09-14

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(n, m):
    global cnt # visited 대신 cnt 사용함 (어차피 다시 되돌아올 일이 없음)
    deq = deque()
    deq.append((n,m))
    while deq:
        n, m = deq.popleft()
        cnt += 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = n+di, m+dj
            if 0<=ni<N and 0<=nj<N and room[ni][nj]-room[n][m]==1:
                deq.append((ni, nj))
                

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0 # 최대 방 개수
    answer = [] # 최대 방 개수가 갱신 될 때, (i, j, cnt) 튜플을 저장할 리스트
    for i in range(N):
        for j in range(N):
            cnt = 0
            bfs(i, j)
            if max_cnt <= cnt:
                max_cnt = cnt
                answer.append((i, j, cnt))
    
    min_value = N**2
    for k in range(len(answer)):
        if answer[k][2] == max_cnt: # answer 리스트에서 cnt 원소가 max_cnt일 때, i, j 원소를 구함 
            if min_value > room[answer[k][0]][answer[k][1]]:
                min_value = room[answer[k][0]][answer[k][1]]

    print('#{} {} {}'. format(tc, min_value, max_cnt))