# 5186_이진수2
# 2022-09-20

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    
    output = ''
    turn = 1
    while turn < 13:
        if N*2 == 1.0:
            output += '1'
            break
        elif N*2 > 1:
            N = N*2 - 1
            output += '1'
            turn += 1
        elif N*2 < 1:
            N = N*2
            output += '0'
            turn += 1

    if turn == 13:
        print('#{}'.format(tc), 'overflow')
    else:
        print('#{} {}'.format(tc, output))

'''
0.625 * 2 = 1.250
0.250 * 2 = 0.5
0.5 * 2 = 1
1로 떨어질 때까지 => (0.101 << 2 생각해보기, 위부터 읽어주기)

0.1 * 2 = 0.2
0.2 * 2 = 0.4
0.4 * 2 = 0.8
0.8 * 2 = 1.6
0.6 * 2 = 1.2
혹은 똑같은 소수점이 나올때까지 반복(무한) => 이 문제에서는 13자리 이상일 때 overflow 출력
'''