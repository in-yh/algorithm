# 2304_창고 다각형(B)
# 2022-09-17

# 앞쪽부터 가장 높은 곳까지 순회하며 높이가 높아질 때마다 갱신 및 현재 높이를 최종값에 더해주기
# 뒤쪽부터 가장 높은 곳까지 순회하며 높이가 높아질 때마다 갱신 및 현재 높이를 최종값에 더해주기
import sys
sys.stdin = open('input.txt', 'r')

N = int(input()) # 기둥개수
H_list = [0]*1001
for _ in range(N):
    L, H = map(int, input().split()) # L 왼쪽면위치, H 높이
    H_list[L] = H

sum_h = 0 # 최종값
pre_h = 0 # 앞쪽부터 순회 전 현재 높이 초기화
for i, h in enumerate(H_list):
    if h == max(H_list): # 가장 높은 곳을 만나면 인덱스 저장 및 높이까지 더해주고 break
        max_i = i
        sum_h += h
        break
    else: # 높이가 높아질 때마다 갱신 및 현재 높이를 최종값에 더해주기
        if pre_h < h:
            pre_h = h
        sum_h += pre_h

pre_h = 0 # 뒤쪽부터 순회 전 현재높이 초기화
for j in range(1000, max_i, -1): # 위에서 구한 '가장 높은 곳의 인덱스' 전까지 순회
    if pre_h < H_list[j]: # 높이가 높아질 때마다 갱신 및 현재 높이를 최종값에 더해주기
        pre_h = H_list[j]
    sum_h += pre_h

print(sum_h)