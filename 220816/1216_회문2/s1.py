# 1216_회문2
# 2022-08-16

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    L = [list(map(str, input())) for _ in range(100)] # 100 x 100

    max_length = 0
    # 행
    for i in range(100):
        for j in range(99):
            if L[i][j] == L[i][j+1]: # j번째와 j+1번째가 같다면
                k = 0
                while k >= 0:
                    if j-k >= 0 and (j+1)+k < 100 and L[i][j-k] == L[i][(j+1)+k]: # j-k번째와 j+1+k번째가 같다면
                        k += 1
                    else:
                        break
                length = 2*k
                if max_length < length:
                    max_length = length

            elif j-1 >= 0 and j+1 < 100 and L[i][j-1] == L[i][j+1]: # j-1번째와 j+1번째가 같다면
                l = 0
                while l >= 0:
                    if j-l >= 0 and j+l < 100 and L[i][j-l] == L[i][j+l]:
                        l += 1
                    else:
                        break
                length = 1 + 2*(l-1)
                if max_length < length:
                    max_length = length

    # 열
    for i in range(100):
        for j in range(99):
            if L[j][i] == L[j+1][i]: # j번째와 j+1번째가 같다면
                m = 0
                while m >= 0:
                    if j-m >= 0 and (j+1)+m < 100 and L[j-m][i] == L[(j+1)+m][i]: # j-m번째와 j+1+m번째가 같다면
                        m += 1
                    else:
                        break
                length = 2*m
                if max_length < length:
                    max_length = length 
                
            elif j-1 >= 0 and L[j-1][i] == L[j+1][i]: # j-1번째와 j+1번째가 같다면
                n = 0
                while n >= 0:
                    if j-n >= 0 and j+n < 100 and L[j-n][i] == L[j+n][i]:
                        n += 1
                    else:
                        break
                length = 1 + 2*(n-1)
                if max_length < length:
                    max_length = length

    print('#{} {}'. format(tc, max_length))