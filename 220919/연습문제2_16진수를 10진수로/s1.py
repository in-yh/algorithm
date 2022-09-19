# 연습문제2_16진수를 10진수로
# 2022-09-19

import sys
sys.stdin = open('input.txt', 'r')

def Bbit_print(i):
    global output
    for j in range(4):
        if i & (1<<j):
            output = '1'+ output
        else:
            output = '0'+ output
    return output


T = int(input())
for _ in range(T):
    string_16 = input() # '0F97A3'
    
    output = ''
    for i in range(len(string_16)):
        Bbit_print((int(string_16, 16)>>(i*4)) & 0xf) # 맨 뒤부터 하나씩 비교
    # output : 000011111001011110100011
    
    for m in range(0, len(output)-len(output)%7, 7):
        sums = 0
        for n in range(7):
            if output[m+n] == '1':
                sums += 1<<(6-n)
        print(sums, end=' ')

    sums = 0
    for m in range(len(output)-len(output)%7, len(output)): # 마지막 남는 거 따로 처리
        if output[m] == '1':
            sums += 1<<(((len(output)%7)-1)-(m%7))           
    print(sums)

# int('0F97A3', 16) => 문자열(16진수)을 정수(10진수)로 변환하기(1021859)