# 1945_간단한 소인수분해
# 2022-08-09

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = b = c = d = e = 0 # 한 번에 0으로 할당
    while N > 1:
        if N % 11 == 0:
            e += 1
            N = N / 11
            continue # if문 한 번 수행하고 올라간 다음 if문 조건에 또 해당되면 다시 수행 
        if N % 7 == 0:
            d += 1
            N = N / 7
            continue
        if N % 5 == 0:
            c += 1
            N = N / 5
            continue
        if N % 3 == 0:
            b += 1
            N = N / 3
            continue
        if N % 2 == 0:
            a += 1
            N = N / 2
            continue
    
    print('#{} {} {} {} {} {}'. format(tc, a, b, c, d, e)) 

    # print('#{}'. format(tc), *etc) 언팩 연산자
    # value = a, b, c, d, e
    # print('#{}'. format(tc), *value)