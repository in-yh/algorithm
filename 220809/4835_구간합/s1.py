# 4835_구간합
# 2022-08-09

import sys
sys.stdin = open('input.txt', 'r')

def sum_list(a, x, y):
    sum_result = 0
    for k in range(x, x + y):
        sum_result += a[k]
    return sum_result

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    maxV = 0
    minV = 10000 * N
    for i in range(N-M+1): # index error 조심
        if sum_list(a, i, M) > maxV:
            maxV = sum_list(a, i, M)
        if sum_list(a, i, M) < minV:
            minV = sum_list(a, i, M)

    result = maxV - minV
    print('#{} {}'. format(t, result))