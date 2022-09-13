# 1265_달란트
# 2022-09-13

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())

    answer = ((N//P)**(P-N%P)) * ((N//P+1)**(N%P))
    print('#{} {}'. format(tc, answer))