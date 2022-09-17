# 5178_노드의 합
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # N 노드의 개수 / M 리프노드의 개수 / L 값을 출력할 노드 번호 
    tree = [0]*(N+1) # 수를 저장할 트리 생성
    for _ in range(M): # 리프노드 번호 / 수
        leafnod, num = map(int, input().split())
        tree[leafnod] = num
    
    # tree 1까지 순회하면서, 만약 0이라면 자식노드 2개(tree[i*2], tree[i*2+1])를 더함
    for i in range(N, 0, -1): # 뒤부터 채워와야 해서 거꾸로 순회
        if tree[i] == 0: 
            if i*2+1<=N: # 오른쪽 자식이 노드의 개수 범위 안이라면(왼쪽,오른쪽 자식 모두 있다면)
                tree[i] = tree[i*2] + tree[i*2+1]
            else: # 오른쪽 자식이 노드의 개수 범위 밖이라면(왼쪽 자식만 있다면)
                tree[i] = tree[i*2]

    print('#{} {}'. format(tc, tree[L]))