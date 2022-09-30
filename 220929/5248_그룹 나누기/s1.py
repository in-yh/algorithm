# 5248_그룹 나누기
# 2022-09-29

import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x # return 위치 잘!!

def union(x, y): # 작은 값이 조상이 되게 하기
    a = find_set(x)
    b = find_set(y)
    if a > b:
        p[a] = b 
    else:
        p[b] = a
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    p = [i for i in range(0, N+1)] # 대표원소 리스트 생성
    for i in range(0, 2*M, 2): # 2개씩 돌려 합치며, 대표원소를 작은 값으로 만들기
        union(arr[i], arr[i+1])

    # 조상 바꿀 때 밑의 것도 바꿔줘야 하는데 그게 안되니깐..
    # 조상을 따로 세주기!
    group = set() 
    for i in range(1, N+1): 
        if p[i] not in group:
            x = find_set(i)
            if x not in group:
                group.add(x)

    print('#{} {}'.format(tc, len(group)))    