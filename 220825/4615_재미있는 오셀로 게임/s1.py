# 4615_재미있는 오셀로 게임
# 2022-08-25

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [[0]*N for _ in range(N)]

    # 시작 시 정가운데 배치
    L[N//2][N//2] = 2
    L[N//2-1][N//2-1] = 2
    L[N//2-1][N//2] = 1
    L[N//2][N//2-1] = 1

    di = [-1, -1, -1, 0, 1, 1, 1, 0]
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]
    for _ in range(M):
        j, i, color = map(int, input().split())
        L[i-1][j-1] = color
        # 자신이 놓을 돌과 8방향 N-1칸 띄운 곳을 탐색했을 때 자신의 돌이 있고, 그 사이에 남의 돌이 있다면, 남의 돌 색깔 모두 바꿔줌
        for k in range(8):
            for s in range(N-1, 1, -1):  # 한 칸 뿐만이 아니라 두 칸, 세 칸 그 이후에도 내 돌이 있고 그 사이에 남의 돌이 있으면 남의 돌 색 다 바꿔줌
                ni = (i-1) + di[k]*s
                nj = (j-1) + dj[k]*s
                cnt = 0
                if 0 <= ni < N and 0 <= nj < N:
                    if L[ni][nj] == color:  # s칸 이후에 내 돌이 있다면
                        for t in range(1, s):  # 그 사이 돌의 색깔이 내 돌 색깔과 다르고 0이 아니라면 cnt 해줌
                             if L[(i-1)+di[k]*t][(j-1)+dj[k]*t] != color and L[(i-1)+di[k]*t][(j-1)+dj[k]*t] != 0:
                                cnt += 1
                        if cnt == s-1:  # 그 사이 돌 색깔 모두가 위 조건에 만족한다면 그 사이의 모든 돌 색깔 바꿔줌
                            for u in range(1, s):
                                L[(i-1)+di[k]*u][(j-1)+dj[k]*u] = color

    # 게임 끝난 후, 흑백돌 개수 출력
    cnt_black = 0
    cnt_white = 0
    for m in range(N):
        for n in range(N):
            if L[m][n] == 1:
                cnt_black += 1
            if L[m][n] == 2:
                cnt_white += 1
    print('#{} {} {}'. format(tc, cnt_black, cnt_white))
