# 5789_현주의 상자 바꾸기
# 2022-08-09

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    list_N = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        list_N[L-1:R] = [i] * (R-L+1) # 인덱스 개수만큼 할당해줘야 함
    print('#{}'. format(tc), *list_N) # 언패킹으로 가능!! *없으면 리스트로 반환됨