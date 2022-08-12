# 9386_연속한 1의 개수
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 10
    L = list(map(int, input())) # [0, 0, 1, 1, 0, 0, 1, 1, 1, 0]

    max_cnt = 0
    cnt = 0
    for i in range(N): # i : 0부터 9까지
        if L[i] == 1: # 1을 만나면 cnt += 1
            cnt += 1
        else: # 0을 만나면 cnt = 0
            if max_cnt < cnt: # 0을 만나기 직전의 cnt값이 max_cnt값보다 크다면,
                max_cnt = cnt # 0을 만나기 직전의 cnt값을 max_cnt에 저장
                cnt = 0 # 그러고 난 후 cnt는 초기화

    if max_cnt < cnt: # 리스트 마지막이 1인 경우에는 cnt만 더하기 1해주고 나오기 때문에 밖에서 max_cnt인지 한 번 더 실행
        max_cnt = cnt

    print('#{} {}'. format(tc, max_cnt))