# 1232_사칙연산
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')

def in_order(s):
    global tree # tree값을 바꿔주기 위해 global 선언
    if tree[s] != '+' and tree[s] != '-' and tree[s] != '*' and tree[s] != '/': # 정수라면
        return s
    elif tree[s] == '+':
        x = in_order(ch1[s])
        y = in_order(ch2[s])
        tree[s] = tree[x] + tree[y]
        return s
    elif tree[s] == '-':
        x = in_order(ch1[s])
        y = in_order(ch2[s])
        tree[s] = tree[x] - tree[y]
        return s
    elif tree[s] == '*':
        x = in_order(ch1[s])
        y = in_order(ch2[s])
        tree[s] = tree[x] * tree[y]
        return s
    elif tree[s] == '/':
        x = in_order(ch1[s])
        y = in_order(ch2[s])
        tree[s] = tree[x] // tree[y]
        return s


for tc in range(1, 11):
    N = int(input()) # 정점 개수
    tree = [0]*(N+1) # 트리 생성
    ch1 = [0]*(N+1) # 부모 인덱스에 자식노드번호 저장
    ch2 = [0]*(N+1)
    for _ in range(N):
        input_list = list(input().split())

        if len(input_list)==4: # 정점이 연산자일 때와 정수일 때 조건 나누기
            Vnum, op, left, right = input_list
            Vnum = int(Vnum)
            left = int(left)
            right = int(right)

            tree[Vnum] = op # [0, '-', '-', 10, 88, 65]
            ch1[Vnum] = left # [0, 2, 4, 0, 0, 0]
            ch2[Vnum] = right # [0, 3, 5, 0, 0, 0]
        else:
            Vnum, integer = input_list
            Vnum = int(Vnum)
            integer = int(integer)
            
            tree[Vnum] = integer

    # 중위순회로 하려했으나.. 그냥 재귀가 됨
    in_order(1)
    print('#{} {}'. format(tc, tree[1]))