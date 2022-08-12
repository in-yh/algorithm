# 9367_점점 커지는 당근의 개수
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    # 리스트를 돌리면서 연속으로 커지면 cnt + 1 하기
    max_cnt = 1 
    cnt = 1 # 최소 길이 1
    for i in range(N-1): # i : 0 -> 3
        if L[i+1] - L[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                cnt = 1

    if max_cnt < cnt: # 리스트 마지막에 연속으로 커지는 경우에도 max_cnt 비교해줘야 함
        max_cnt = cnt

    print('#{} {}'. format(tc, max_cnt))
