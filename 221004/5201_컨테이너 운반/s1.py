# 5201_컨테이너 운반
# 2022-10-03

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    container.sort(reverse=True)
    truck = list(map(int, input().split()))
    truck.sort(reverse=True)
    
    sum_c = 0
    for c in container:
        for idx, t in enumerate(truck):
            if c <= t:
                sum_c += c
                truck.pop(idx)
                break
    print('#{} {}'.format(tc, sum_c))