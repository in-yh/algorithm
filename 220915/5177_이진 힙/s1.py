# 5177_이진 힙
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 노드 개수
    nums = list(map(int, input().split())) # 차례대로 입력되는 수

    tree = [0]*(N+1) # 트리 생성

    # num 입력 받을 때마다 tree에 순서대로 입력
    # 부모노드(N//2) 숫자와 비교후 num이 더 작으면 자리 바꿈
    for idx, num in enumerate(nums):
        tree[idx+1] = num
        if idx+1 >= 2: # 루트노드는 제외
            # 마지막에 제일 작은 숫자가 들어온다면 루트까지 더 위로 올라가서 바꿔줘야 함
            while (idx+1)//2 >= 1:
                if tree[(idx+1)//2] > tree[idx+1]:
                    tree[(idx+1)//2], tree[idx+1] = tree[idx+1], tree[(idx+1)//2]
                    idx = (idx+1)//2 - 1
                else:
                    break 

    # 마지막 노드의 조상 노드에 저장된 정수의 합 / 마지막 노드 숫자 : tree[N]
    answer = 0
    while N//2 >= 1:
        answer += tree[N//2]
        N = N//2

    print('#{} {}'. format(tc, answer))