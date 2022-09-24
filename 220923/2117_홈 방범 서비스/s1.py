# 2117_홈 방범 서비스
# 2022-09-23

import sys
sys.stdin = open('input.txt', 'r')

# 영역 구하기
def bfs(sti, stj, k):
    global cnt
    q = []
    visited = [[0]*N for _ in range(N)]
    q.append((sti,stj))
    visited[sti][stj] = 1
    while q:
        i, j = q.pop(0)
        if abs(sti-i) + abs(stj-j) > k-1: # 범위 설정 잘 해야 함
            break

        if home[i][j] == 1:
            cnt += 1

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 도시크기 / M 집이 지불하는 비용
    home = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(1, N+2): # N이 짝수일때는 k가 N+1까지 돌아야 함
                cnt = 0
                bfs(i, j, k)
                if ((M*cnt) - (k*k+(k-1)*(k-1))) >= 0:
                    if max_cnt < cnt:
                        max_cnt = cnt

    print('#{} {}'.format(tc, max_cnt))