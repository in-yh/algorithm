# 5204_병합 정렬
# 2022-09-27

import sys
sys.stdin = open('input.txt', 'r')

# 분할과정
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# 병합과정
def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1

    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) or right_idx < len(right):
        if left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        elif left_idx < len(left):
            result += left[left_idx:]
            left_idx = len(left) # 여기서도 idx늘려줘야 돼
        elif right_idx < len(right):
            result += right[right_idx:]
            right_idx = len(right)
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    answer = merge_sort(A)
    print('#{} {} {}'.format(tc, answer[N//2], cnt))