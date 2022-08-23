# 2075_N번째 큰 수(B)
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

nums = []
for _ in range(N):
    nums += list(map(int, input().split())) # 한줄 씩 리스트로 받기
nums.sort() # 정렬..

print(nums[-N])