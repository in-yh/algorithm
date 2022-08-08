# 1206_view
# 2022-08-08

# 정답코드
import sys # 내장모듈은 사용가능
sys.stdin = open('input.txt', 'r') # 확장자까지 써야함, read

def maximum(a, b, c, d):
    max_list = [a, b, c, d]
    max_num = max_list[0]
    for i in range(1, 4):
        if max_num < max_list[i]:
            max_num = max_list[i]
    return max_num

for t in range(1, 11):
    N = int(input())
    L = list(map(int, input().split()))

    sums = 0
    for i in range(2, (N-2)):
        if (L[i] > L[i-1]) and (L[i] > L[i-2]) and (L[i] > L[i+1]) and (L[i] > L[i+2]):
            sums += (L[i] - maximum(L[i-2], L[i-1], L[i+1], L[i+2]))
        
    print(f'#{t} {sums}')

# T = int(input()) # 가장 첫줄
# for tc in range(1, 10+1):
    # map사용해서 test 다 받아오기
    # 문제 풀기