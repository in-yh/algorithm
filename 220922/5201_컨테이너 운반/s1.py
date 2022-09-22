# 5201_컨테이너 운반
# 2022-09-22

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 컨테이너수 / M 트럭수
    N_weight = list(map(int, input().split())) # 컨테이너 무게 
    M_capacity = list(map(int, input().split())) # 트럭 적재용량

    # 컨테이너 무게 큰것부터 sort
    N_weight.sort(reverse=True)
    
    # 가장 큰 화물이 들어갈 수 있니?
    # 없으면 pass
    # 있으면 화물값을 결과값에 더해주고 트럭은 제외시킴(used를 1(사용)로 바꿈)
    # 반복
    result = 0
    used = [0]*M
    for i in range(N):
        for j in range(M):
            if used[j]==0 and N_weight[i]<=M_capacity[j]:
                result += N_weight[i]
                used[j] = 1
                break # 한 번 찾으면 i로 돌아감
    
    print('#{} {}'.format(tc, result))