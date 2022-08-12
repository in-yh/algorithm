# 1210_ladder1
# 2022-08-11

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    L = [list(map(int, input().split())) for _ in range(100)]

    for k in range(100):
        if L[99][k] == 2: # 도착지점의 열 인덱스를 저장
            j = k

    i = 99
    while i > 0: # i가 0에 도달할 때 멈춤
        if j+1 < 100 and L[i][j+1] == 1: # j+1이 100을 초과하지 않을 때 & 오른쪽이 1일 때 (순서 바꾸면 안돼!! j+1<100을 먼저 보고 여기서 거짓이면 뒤는 보지 않음.(단축평가!!) 자리 바꾸면 indexerror 발생)
            while L[i][j+1] == 1: # 오른쪽이 1이 아닐 때까지 j에 +1 해줌, 여기서 indexerror 발생하지 않도록(j가 99번까지 1인 경우) 아래 if문으로 나눠줌
                if j < 98: # j는 최대 97
                    j += 1 # j는 98, 이 상태로 while문 들어가면 L[i][99] 가능 
                else: # L[i][99] == 1 가능하므로 그 때 j = 98으로 else문으로 들어오게 됨.
                    j += 1 # 여기서 한 번 더 j+1 해줘야 j가 99 나올 수 있음!!
                    break # break 시켜주지 않으면 j가 99로 while문에 들어가 또 indexerror 발생
            i -= 1 # 다 하고 한 칸 상승시켜주기
        elif j-1 > 0 and L[i][j-1] == 1: # j-1이 0 미만이지 않을 때 & 왼쪽이 1일 때
            while L[i][j-1] == 1:
                if j > 1:
                    j -= 1
                else:
                    j -= 1
                    break
            i -= 1
        else:
            i -= 1 # 오른쪽, 왼쪽 모두 0이면 그냥 위로 올라감

    print('#{} {}'. format(tc, j))