# 2075_N번째 큰 수(B)
# 2022-08-24

import sys
import heapq
sys.stdin = open('input.txt', 'r')

N = int(input())
heap = []

for _ in range(N):
    numbers = list(map(int, input().split())) # 한 행씩 받음

    if not heap:
        for num in numbers:
            heapq.heappush(heap, num) # [5, 7, 9, 15, 12] 완전히 오름차순 정렬이 되는 것은 아님
    else:
        for num in numbers:
            if heap[0] < num:
                heapq.heappush(heap, num) # num 들어온 후 자동으로 오름차순 정렬됨(완벽한 것은 아니지만)
                heapq.heappop(heap) # 그래서 가장 작은 값(heap[0])이 pop 됨
                # 모든 값들을 들어옴으로써
                # heap[0]보다 크면 push하고(heap[0]보다 작으면 어차피 버리면 됨)
                # heap[0]이 가장 작은 값인데 pop을 한다.
                # 즉, heap을 가장 큰 수 5개로 유지한다.

print(heap[0]) # heap은 5개로 그 중 가장 작은 값, 즉 5번째로 큰 수 출력