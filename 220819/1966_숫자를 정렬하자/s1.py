# 1966_숫자를 정렬하자
# 2022-08-19

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    
    for i in range(N-1): # 선택정렬
        minIdx = i
        for j in range(i+1, N):
            if L[minIdx] > L[j]:
                minIdx = j
        L[i], L[minIdx] = L[minIdx], L[i]
    
    print('#{}'. format(tc), *L)