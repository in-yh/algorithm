# 4828_min-max
# 2022-08-09

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    
    maxV = L[0]
    minV = L[0]
    for i in range(N): # 한 번에 돌려도 됨
        if L[i] > maxV:
            maxV = L[i]
        if L[i] < minV:
            minV = L[i]

    result = maxV - minV
    print('#{} {}'. format(t, result)) # format 쓰기!!