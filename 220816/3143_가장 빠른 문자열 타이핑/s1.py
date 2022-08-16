# 3143_가장 빠른 문자열 타이핑
# 2022-08-16

import sys
sys.stdin = open('input.txt', 'r')

def length(str):
    cnt = 0
    for s in str:
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split()) # banana, bana
    N = length(A) # 6
    M = length(B) # 4

    cnt = 0
    i = 0
    while i < N: # 0~5 / i 순서대로 코드를 짜야하는 듯
        if A[i:i+M] == B:
            cnt += 1
            i += M
        else:
            cnt += 1
            i += 1

    print('#{} {}'. format(tc, cnt))