# 연습문제1_Gravity
# 2022-08-08

'''
3 # 테스트 케이스 T의 개수
9 # 상자 개수
7 4 2 0 0 6 0 7 0 # 상자들이 쌓여 있는 높이
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
'''

def cnt(x, y, list):
    sums = 0
    for a in list[x-1:]:
        if a >= y: # y도 포함되어야 하기에 등호 사용해야 함
            sums += 1
    return sums

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_h = 0
    for i in range(1, N+1):
        for j in range(1, (arr[i-1]+1)): # index error 조심..
            h = N-(i-1) - cnt(i, j, arr) # cnt : i이상이면서 j이상인 개수
            if h > max_h:
                max_h = h
    print(f'#{t} {max_h}')