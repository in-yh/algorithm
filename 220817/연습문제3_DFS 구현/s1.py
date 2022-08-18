# 연습문제3_DFS 구현
# 2022-08-17

import sys
sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split()) # 7, 8
A = list(map(int, input().split())) # [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
adjust = [[] for _ in range(N)] # 2차원 배열로 인접한 정점 리스트 만듦

for i in range(0, len(A), 2): # 짝수 인덱스는 시작점, 홀수 인덱스는 끝점
    adjust[A[i]-1].append(A[i+1])
    adjust[A[i+1]-1].append(A[i])
    
def dfs(v, N):
    visited = [0]*(N+1) # 인덱스 혼란 방지
    stack = [0]*N
    top = -1
    result = []

    visited[v] = 1 # 시작 정점
    result.append(v)
    while True: # 무한 반복
        for w in adjust[v-1]: # 시작정점 기준으로 for문 돌리기
            if visited[w] == 0: # 인접한 곳이 아직 안 간 곳이라면
                top += 1 # push(v)!!
                stack[top] = v
                v = w
                result.append(v)
                visited[v] = 1 # visited 1로 바꿔줌
                break # 다른 곳으로 옮겼다면 break!!
        else: # 인접한 곳을 다 갔다면
            if top != -1: # stack이 비어있지 않다면, top으로 표현하기!!
                v = stack[top] # pop
                top -= 1
            else: # stack이 비어있다면
                break

    return result

# 숫자를 문자로 바꿔서 join!!
# list_dfs = dfs(1, N)
# answer = ' '.join(map(str, list_dfs)) 
# print(answer)

# *list도 가능함
print(*dfs(1, N))