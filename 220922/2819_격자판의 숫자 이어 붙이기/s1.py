# 2819_격자판의 숫자 이어 붙이기
# 2022-09-22

import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, j, cnt, value): # 4개 인자로 받아서.. 내가 한 건 왜 안되는지 이유를 모르겠음(아이디어는 똑같은데..)
    if cnt == 7:
        result.add(value) # set이기에 add메서드 사용
        return
    else:
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<4 and 0<=nj<4: 
                dfs(ni, nj, cnt+1, value+board[ni][nj])


T = int(input())
for tc in range(1, T+1):
    board = [list(map(str, input().split())) for _ in range(4)] 
    # [['1', '1', '1', '1'], ['1', '1', '1', '2'], ['1', '1', '2', '1'], ['1', '1', '1', '1']]

    result = set() # 중복 제거 위해 set으로 정의
    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, board[i][j])

    answer = len(result)  
    print('#{} {}'.format(tc, answer))