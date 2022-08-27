# 2491_수열(B)
# 2022-08-27

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
L = list(map(int, input().split()))
max_cnt = 1 # 이거 안바꿔서..?

# 증가할 때 가장 긴 길이
cnt = 1
for i in range(N-1):
    if L[i] <= L[i+1]:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1

# 감소할 때 가장 긴 길이
cnt = 1
for j in range(N-1):
    if L[j] >= L[j+1]:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1

print(max_cnt)