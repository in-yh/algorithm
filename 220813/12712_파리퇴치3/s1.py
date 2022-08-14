# 12712_파리퇴치3
# 2022-08-13

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]

    # 십자모양
    di = [0, 1, 0, -1]
    dj = [1, 0, -1,0]

    max_sum = 0
    # 중심을 구하고 중심의 유효한 4방향 값 더하기
    for i in range(N): # 0부터 N-1까지 끝까지 돌려야 함, 중심이 L[N-1][N-1]까지!, 어차피 유효하지 않은 인덱스는 아래에서 제거 예정
        for j in range(N):
            sum_10 = L[i][j] # 중심 값을 초기값으로 설정
            # M칸씩 찾기
            for m in range(1, M): # 1부터 M-1까지 돌려야 함
                for k in range(4):
                    ni = i + di[k]*m
                    nj = j + dj[k]*m
                    if 0 <= ni < N and 0 <= nj < N: # 유효한 값만 추출
                        sum_10 += L[ni][nj]
            if max_sum < sum_10:
                max_sum = sum_10

    # 대각선모양
    di = [-1, 1, 1, -1]
    dj = [1, 1, -1, -1]

    for i in range(N):
        for j in range(N):
            sum_x = L[i][j]
            for m in range(1, M):
                for k in range(4):
                    ni = i + di[k]*m
                    nj = j + dj[k]*m
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_x += L[ni][nj]
            if max_sum < sum_x:
                max_sum = sum_x
                            
    print('#{} {}'. format(tc, max_sum))