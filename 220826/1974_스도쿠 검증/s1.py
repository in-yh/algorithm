# 1974_스도쿠 검증
# 2022-08-26

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    L = [list(map(int, input().split())) for _ in range(9)]

    # 행 검사
    result1 = -1
    cnt = 0
    for i in range(9):
        check = []
        for j in range(9):
            check.append(L[i][j])
        check.sort() # sort 해주기!!
        if check == list(range(1, 10)):
            cnt += 1
        else:
            result1 = 0
            break
    if cnt == 9:
        result1 = 1

    # 열 검사
    result2 = -1
    cnt = 0
    for j in range(9):
        check = []
        for i in range(9):
            check.append(L[i][j])
        check.sort()
        if check == list(range(1, 10)):
            cnt += 1
        else:
            result2 = 0
            break
    if cnt == 9:
        result2 = 1

    # 사각형 검사
    result3 = -1

    di = [-1, -1, -1, 0, 1, 1, 1, 0]
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]

    cnt = 0
    for i in range(1, 9, 3):
        for j in range(1, 9, 3):
            check = [L[i][j]]
            for k in range(8):
                ni, nj = i + di[k], j + dj[k]
                check.append(L[ni][nj])
            check.sort()
            if check == list(range(1, 10)):
                cnt += 1
            else:
                result3 = 0
                break
    if cnt == 9:
        result3 = 1

    # 각각의 result값으로 최종 정답 출력
    result = -1
    if result1 == 1 and result2 == 1 and result3 == 1:
        result = 1
    else:
        result = 0
    print('#{} {}'. format(tc, result))