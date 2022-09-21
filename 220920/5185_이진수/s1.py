# 5185_이진수
# 2022-09-20

import sys
sys.stdin = open('input.txt', 'r')

def Change_Binary(i):
    global output
    for j in range(4):
        if i & (1<<j):
            output = '1' + output
        else:
            output = '0' + output


T = int(input())
for tc in range(1, T+1):
    N, str_16 = input().split()
    N = int(N)
    str_16 = int(str_16, 16) # '47FE'(16진수)를 18430(10진수)로 바꿔줌
    
    output = '' # 최종값
    for k in range(N):
        Change_Binary(str_16>>k*4 & 0xf) # 뒤부터 하나씩 빼서 2진수로 바꿈
    
    print('#{} {}'. format(tc, output))