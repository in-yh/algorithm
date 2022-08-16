# 4864_문자열 비교
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
    N = length(str1) # 4
    str2 = input()
    M = length(str2) # 10

    for i in range(M-N+1): # range(7)
        if str2[i:i+N] == str1:
            result = 1
            break # break 안하면 이후 i에서 result가 0이 될 수 있음
        else:
            result = 0
    
    print('#{} {}'. format(tc, result))