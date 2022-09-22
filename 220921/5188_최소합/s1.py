# 5188_최소합
# 2022-09-21

import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, j, n):
    global visited
    global p
    global minV
    if (i, j) == (n-1, n-1): # 맨 오른쪽 아래라면 리턴
        if minV > sum(p):
            minV = sum(p)
        return
    
    if sum(p) > minV: # 백트래킹 안하면 시간초과 남
        return

    else:
        visited[i][j] = 1
        for di, dj in [[0,1],[1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
                p.append(L[ni][nj])
                dfs(ni, nj, n)
                visited[ni][nj] = 0 # dfs돌아오면 갔던 곳 미방문으로 처리해야 다른 방법 구할 수 있음
                p.pop() # 돌아오고 나면 p에서도 빼줌


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    p = [L[0][0]] # 맨 왼쪽 위는 미리 넣어줌
    minV = 13*13*10
    dfs(0, 0, N)

    print('#{} {}'.format(tc, minV))