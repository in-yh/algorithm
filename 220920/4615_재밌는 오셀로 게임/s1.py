# 4615_재밌는 오셀로 게임
# 2022-09-20

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 한 변의 길이 / M 돌을 놓는 횟수
    board = [[0]*N for _ in range(N)] # N X N board
    board[N//2][N//2] = 2 # 중앙 배치
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    
    for _ in range(M):
        J, I, color = map(int, input().split())
        i = I-1
        j = J-1
        board[i][j] = color
        for di, dj in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
            for k in range(N-1, 1, -1):
                ni, nj = i+di*k, j+dj*k
                if 0<=ni<N and 0<=nj<N and board[ni][nj] == color:
                    cnt = 0
                    l = 1
                    while l < k:  
                        ni, nj = i+di*l, j+dj*l
                        if 0<=ni<N and 0<=nj<N and board[ni][nj] != 0 and board[ni][nj] != color:
                            cnt += 1
                            l += 1
                        else:
                            break
                    if cnt == k-1:
                        for a in range(1, k):
                            ni, nj = i+di*a, j+dj*a
                            board[ni][nj] = color
                            
    cnt_black = 0
    cnt_white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt_black += 1
            elif board[i][j] == 2:
                cnt_white += 1

    print('#{} {} {}'. format(tc, cnt_black, cnt_white))