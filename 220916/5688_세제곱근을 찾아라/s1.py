# 5688_세제곱근을 찾아라
# 2022-09-16

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for i in range(1, 10**6+1): # 범위조심
        if i**3 == N:
            answer = i
            break
    else:
        answer = -1

    print('#{} {}'. format(tc, answer))