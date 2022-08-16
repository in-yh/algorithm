# 5356_의석이의 세로로 말해요
# 2022-08-16

import sys
sys.stdin = open('input.txt', 'r')

def length(my_list):
    l = 0
    for _ in my_list:
        l += 1
    return l

T = int(input())
for tc in range(1, T+1):
    L = [list(map(str, input())) for _ in range(5)]

    max_l = 0
    for i in range(5): # 5개의 단어 중 가장 긴 길이 구하기
        l = length(L[i])
        if max_l < l:
            max_l = l

    s = ''
    for j in range(max_l): # 0~5
        for i in range(5): # 0~4
            if length(L[i]) > j: # L[i]의 길이가 j보다 크다면 / length(L[1])=4 > 3
                s += L[i][j] # L[1][3]까지만 됨
                
    print('#{} {}'. format(tc, s))