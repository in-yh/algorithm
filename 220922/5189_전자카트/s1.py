# 5189_전자카트
# 2022-09-22

import sys
sys.stdin = open('input.txt', 'r')

def f(i, k):
    global route
    if i == k:
        route.append(p[:]) # 얕은 복사 되지 않게 주의..
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]
    route = []
    f(1, N) # 인덱스 0은 고정 후 순열 구해주기
   
    minb = 100 * N * N
    for r in route:
        sumb = 0
        for i in range(N):
            if i == N-1:
                sumb += battery[r[i]][0]
            else:
                sumb += battery[r[i]][r[i+1]]
     
        if minb > sumb:
            minb = sumb

    print('#{} {}'.format(tc, minb))