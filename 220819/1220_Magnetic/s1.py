# 1220_Magnetic
# 2022-08-19

# 2차원 배열에서 열순회를 먼저 하면서
    # N(1)을 만나면
        # 그 다음 값으로 S(2)를 만나면
            # result += 1
        # 그 다음 값으로 N(1)을 만나면
            # N값 교체

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    square_length = int(input())
    square_list = [list(map(int, input().split())) for _ in range(square_length)]
    result = 0 # 교착상태 개수 초기값

    for j in range(square_length):
        i = 0
        while i < square_length-1: # 범위 하나 줄여서!! 아래에서 어차피 i+1과 비교를 하기 때문에 굳이 100까지 설정할 필요 없음!! 100까지 설정하면 무한루프 나옴..
            if square_list[i][j] == 1:
                k = i+1
                while k < square_length:
                    if square_list[k][j] == 2:
                        result += 1
                        i = k+1
                        break 
                    elif square_list[k][j] == 1:
                        i = k
                        break
                    elif square_list[k][j] == 0:
                        k += 1
                        i = k # 마지막에 0으로 끝나는 경우가 있기 때문에 i를 설정해줘야 함. k가 99일 때 k는 탈출하나 i가 탈출 안 됨.
            else:
                i += 1
    
    print('#{} {}'. format(tc, result))