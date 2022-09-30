# 5247_연산2
# 2022-09-28

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def BFS(x, y):
    global result
    q = deque()
    q.append((x, 0))
    visited = [0]*1000001
    visited[x] = 1
    while q:
        a, cnt = q.popleft()
        if a == y:
            result = min(result, cnt)
            return

        if 0 < a+1 <= 1000000 and visited[a+1]==0: # 범위설정 하는 것과 방문 표시 해줘야 함
            q.append((a+1, cnt+1))
            visited[a+1] = 1
        if 0 < a-1 <= 1000000 and visited[a-1]==0:
            q.append((a-1, cnt+1))
            visited[a-1] = 1
        if 0 < a*2 <= 1000000 and visited[a*2]==0:
            q.append((a*2, cnt+1))
            visited[a*2] = 1
        if 0 < a-10 <= 1000000 and visited[a-10]==0:
            q.append((a-10, cnt+1))
            visited[a-10] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    result = 1000000
    BFS(N, M)
    print('#{} {}'.format(tc, result))