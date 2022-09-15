# 5174_subtree
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')

# 전위순회 하면서 노드개수 카운트하고, 자식이 0이면 노드개수 리턴
def preorder(s):
    global cnt
    if s:
        cnt += 1
        preorder(ch1[s])
        preorder(ch2[s])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # E : 간선개수 / N : 시작노드
    V = E + 1 # V : 노드 개수
    edge_list = list(map(int, input().split()))

    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)

    for i in range(0, E*2, 2):
        if ch1[edge_list[i]] == 0:
            ch1[edge_list[i]] = edge_list[i+1]
        else:
            ch2[edge_list[i]] = edge_list[i+1]

    cnt = 0
    preorder(N)

    print('#{} {}'. format(tc, cnt))