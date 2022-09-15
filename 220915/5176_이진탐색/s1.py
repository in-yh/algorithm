# 5176_이진탐색
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')

def in_order(s):
    global num
    if s<=N: # N보다 작거나 같을 때 수행
        in_order(s*2)
        tree[s] = num
        num += 1
        in_order(s*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N 노드개수

    # 중위순회하면서 숫자 넣기
    tree = [0]*(N+1) # 숫자를 넣을 tree 생성(인덱스가 루트 번호)
    num = 1 # tree에 넣을 숫자
    in_order(1)

    print('#{} {} {}'. format(tc, tree[1], tree[N//2]))