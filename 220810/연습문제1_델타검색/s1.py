# 연습문제1_델타검색
# 2022-08-10

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0] # 여기에 선언!

    sum_forth = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] - arr[i][j] >= 0:
                        sum_forth += arr[ni][nj] - arr[i][j]
                    else:
                        sum_forth += -(arr[ni][nj] - arr[i][j])
    print('#{} {}'. format(tc, sum_forth))

# % 넣어서 해보기