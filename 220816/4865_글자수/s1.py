# 4865_글자수
# 2022-08-16

import sys
sys.stdin = open('input.txt', 'r')

def length(str):
    cnt = 0
    for s in str:
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    N = length(str1)
    str2 = input()
    M = length(str2)

    dict2 = dict()
    for s2 in str2: # EOGGXYPVSY
        if s2 in dict2: # s가 딕셔너리 안에 있으면 추가
            dict2[s2] += 1
        else: # s가 딕셔너리 안에 없으면 새로 생성
            dict2[s2] = 1

    maxV = 0
    for s1 in str1:
        if dict2[s1] > maxV:
            maxV = dict2[s1]
    
    print('#{} {}'. format(tc, maxV))