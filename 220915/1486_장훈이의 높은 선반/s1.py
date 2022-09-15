# 1486_장훈이의 높은 선반
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) # N 점원수 / B 선반높이
    H = list(map(int, input().split())) # 점원들의 키

    # 부분집합 구해 각각의 합을 리스트 저장
    # 리스트에서 B보다 크거나 같으면서 최소값 찾기
    H_subset = [[] for _ in range(1<<N)]
    for i in range(1<<N): # 1<<N = 2^N / 0~31
        for j in range(N): # 0~4
            if i & (1<<j): # i가 7일 때, j가 0,1,2이면 참
                H_subset[i].append(H[j])
        H_subset[i] = sum(H_subset[i]) 

    min_value = sum(H)
    value = sum(H)
    for h in H_subset:
        if h >= B:
            value = h-B
            if min_value > value:
                min_value = value

    print('#{} {}'. format(tc, min_value))