# 5189_전자카트
# 2022-10-03

import sys
sys.stdin = open('input.txt', 'r')

def p(i, n):
    if i == n:
        result.append(arr[:]) # 복사 주의
        return
    else:
        for j in range(i, n):
            arr[i], arr[j] = arr[j], arr[i]
            p(i+1, n)
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    # 앞뒤 1은 고정, 가운데 순열로 모든 경우의 수 구하기
    arr = [i for i in range(N)]
    result = []
    p(1, N)
    
    # 최소 배터리 소비량 구하기
    minV = 10*10*100
    for r in result:
        sum_battery = 0
        for idx, value in enumerate(r):
            if idx == len(r)-1: # 마지막 인덱스일 때
                sum_battery += battery[r[idx]][0]
            else: 
                sum_battery += battery[r[idx]][r[idx+1]]

        if minV > sum_battery:
            minV = sum_battery
    
    print('#{} {}'.format(tc, minV))