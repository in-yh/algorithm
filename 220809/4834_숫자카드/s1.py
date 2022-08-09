# 4834_숫자카드
# 2022-08-09

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    a = list(map(int, input()))

    c = [0]*10
    for i in range(N):
        c[a[i]] += 1 # 카운팅 정렬
    
    mxm_cnt = c[0]
    for j in range(1, 10):
        if c[j] >= mxm_cnt:
            mxm_cnt = c[j]
            mxm_val = j
    
    print('#{} {} {}'. format(t, mxm_val, mxm_cnt))