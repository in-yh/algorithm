# 4869_종이 붙이기
# 2022-08-18

import sys
sys.stdin = open('input.txt', 'r')

def fibo_paper(N):
    # N이 10일 때, 1가지
    if N == 10:
        return 1
    # N이 20일 때, 3가지
    elif N == 20:
        return 3
    # N이 30이상일 때, 2*(N-2)번째 + (N-1)번째
    elif N >= 30:
        return 2*fibo_paper(N-20) + fibo_paper(N-10)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print('#{} {}'. format(tc, fibo_paper(N)))