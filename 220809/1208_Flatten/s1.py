# 1208_Flatten
# 2022-08-09

import sys
sys.stdin = open('input.txt', 'r')

def mxm_list(a):
    mxm = 0
    for j in range(100):
        if a[j] > mxm:
            mxm = a[j]
            mxm_idx = j
    return mxm, mxm_idx

def mnm_list(a):
    mnm = 101
    for j in range(100):
        if a[j] < mnm:
            mnm = a[j]
            mnm_idx = j
    return mnm, mnm_idx

for tc in range(1, 11):
    dump = int(input())
    h = list(map(int, input().split()))

    for i in range(dump):
        # 가장 높은 숫자-1, 가장 낮은 숫자+1
        h[mxm_list(h)[1]] -= 1
        h[mnm_list(h)[1]] += 1
        # 가장 높은 숫자 - 가장 낮은 숫자 <= 1 이면, break
        if mxm_list(h)[0] - mnm_list(h)[0] <= 1:
            break
    
    # (가장 높은 숫자 - 가장 낮은 숫자) 반환
    print('#{} {}'. format(tc, mxm_list(h)[0] - mnm_list(h)[0]))