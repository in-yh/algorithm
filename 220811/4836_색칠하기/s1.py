# 4836_색칠하기
# 2022-08-11

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [[0]*10 for _ in range(10)]
    cnt = 0 # cnt 값을 N 돌리기 전에 넣어야 함. N 이후에 넣으면 한 박스 색칠 할 때마다 cnt 초기화 됨.
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if L[i][j] == 0: # L[i][j] 흰색이라면 
                    L[i][j] = color # color(빨간색 혹은 파란색) 넣어주기
                elif L[i][j] != color: # L[i][j] 흰색 아니고 color값이 있는데, 내가 칠할 color랑 다르다면
                    L[i][j] = 3 # 보라색으로 내가 임의의 값 지정, 어차피 이미 색칠한 위치에 같은 색 겹쳐서 칠할 수 없음.
                    cnt += 1
    
    print('#{} {}'. format(tc, cnt))