# 1209_SUM
# 2022-08-10

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxV = 0 # 최대 행의 합
    for i in range(100):
        s1 = 0 # 행의 합, j 다 돌때마다 초기화
        s2 = 0 
        for j in range(100):
            s1 += arr[i][j] # i행의 j열 접근
            s2 += arr[j][i] # j열의 i행 접근
            if s1 > maxV: # 하나의 for문에 두 가지 비교
                maxV = s1
            if s2 > maxV:
                maxV = s2

    s3 = 0
    for k in range(100):
        s3 += arr[k][k] # for문 하나 쓰면서 대각선 합 구하기
        if s3 > maxV:
            maxV = s3
    
    s4 = 0
    for l in range(100):
        s4 += arr[l][99-l] # 반대 대각선은 100-1-l 로!
        if s4 > maxV:
            maxV = s4
        
    print('#{} {}'. format(tc, maxV))