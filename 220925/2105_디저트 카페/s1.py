# 2105_디저트 카페
# 2022-09-25

import sys
sys.stdin = open('input.txt', 'r')

di = [1, 1, -1, -1] # 대각선 방향
dj = [1, -1, -1, 1]

def DFS(i, j, d, cnt): # d 방향 / cnt 진행한 칸수
    global result
    global sti, stj

    if d==3 and (i, j) == (sti, stj): # 출발점에 도착한 경우
        result = max(result, cnt)
        return

    elif i<0 or i>=N or j<0 or j>=N: # 범위 밖
        return

    elif dessert[i][j] in eated: # 먹었던 디저트 숫자 저장해놓고 같은 디저트를 파는 곳이면 가지 않는다
        return

    else: # 갈 수 있는 곳
        eated.append(dessert[i][j])
        if d==0 or d==1: # 오른쪽 방향 그대로 가거나 왼쪽으로 꺾었을 경우
            DFS(i+di[d], j+dj[d], d, cnt+1) # 방향 그대로 쭉 가는 것
            DFS(i+di[d+1], j+dj[d+1], d+1, cnt+1) # 방향 꺾음
        elif d==2:
            if i+j != sti+stj: # 출발점을 향하는게 아님(도착할 수 있는 경우가 아닐 때)
                DFS(i+di[2], j+dj[2], d, cnt+1) # 그냥 쭉 가
            else:
                DFS(i+di[3], j+dj[3], d+1, cnt+1) # 방향 꺾어서 가
        else: # k가 3일 때는 직진한다.
            DFS(i+di[3], j+dj[3], d, cnt+1)
        eated.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    eated = []
    for i in range(N):
        for j in range(1, N):
            eated.append(dessert[i][j])
            sti, stj = i, j
            DFS(i+1, j+1, 0, 1)
            eated.pop()

    print('#{} {}'.format(tc, result)) 
# 구글링..