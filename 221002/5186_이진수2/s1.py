# 5186_이진수2
# 2022-10-01

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    result = ''
    i = 1
    while i < 13:
        if N*2 == 1:
            result += '1'
            break
        elif N*2 > 1:
            result += '1'
            N = N*2 - 1 # N값 바꿔줘야 함
            i += 1
        elif N*2 < 1:
            result += '0'
            N = N*2
            i += 1

    if i >= 13: # 13 이상이면 'overflow' 출력
        print('#{} {}'.format(tc, 'overflow'))
    else:
        print('#{} {}'.format(tc, result))