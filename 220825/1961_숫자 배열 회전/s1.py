# 1961_숫자 배열 회전
# 2022-08-25

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 첫 행부터 읽은 후 N-1열에 넣기
    rotation_90 = ['']*N # 90도 회전 후의 리스트(초기값)
    for i in range(N):
        string = ''.join(list(map(str, input().split()))) # 123
        for idx1, num1 in enumerate(string):
            rotation_90[idx1] = num1 + rotation_90[idx1]
    # rotation_90 = ['741', '852', '963']

    rotation_180 = ['']*N # 180도 회전 후의 리스트(초기값)
    for j in range(N):
        for idx2, num2 in enumerate(rotation_90[j]):
            rotation_180[idx2] = num2 + rotation_180[idx2]
    # rotation_180 = ['987', '654', '321']

    rotation_270 = ['']*N # 270도 회전 후의 리스트(초기값)
    for k in range(N):
        for idx3, num3 in enumerate(rotation_180[k]):
            rotation_270[idx3] = num3 + rotation_270[idx3]
    # rotation_270 = ['369', '258', '147']

    print('#{}'. format(tc))
    for l in range(N):
        print(rotation_90[l], rotation_180[l], rotation_270[l])