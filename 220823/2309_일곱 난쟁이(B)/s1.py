# 2309_일곱 난쟁이(B)
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')

L = [] # 9명의 난쟁이 키 담을 리스트
sum_num = 0 # 9명의 난쟁이 키의 합(초기값)
for _ in range(9):
    num = int(input())
    L.append(num)
    sum_num += num # sum_num : 140

for m in range(8):
    for n in range(m+1, 9):
        if L[m] + L[n] == sum_num - 100: # 2명의 거짓 난쟁이들 키의 합이 40일 때
            x, y = m, n # 할당해준 후 밖에서 pop하기! 안에서 pop하면 인덱스 에러 남!
            break
L.pop(y)
L.pop(x)

L.sort() # 선택정렬로도 가능

for k in range(7):
    print(L[k])