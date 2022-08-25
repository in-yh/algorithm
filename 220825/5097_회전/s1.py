# 5097_회전
# 2022-08-25

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    for _ in range(M):
        a = Q.pop(0)
        Q.append(a)

    print('#{} {}'. format(tc, Q[0]))
