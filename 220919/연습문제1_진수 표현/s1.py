# 연습문제1_진수 표현
# 2022-09-19

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    bit_string = input() # 00000010001101
    answer_list = [] # 최종값
    for i in range(0, len(bit_string), 7): # 7개씩 끊어내기 위해 7개 중 최초값을 i로 설정
        answer = 0 # 7개의 합 넣을 변수
        for j in range(7): # 최초값부터 7개씩 순회하며, 1이면 2^(6-j)을 더해준다.
            if bit_string[i+j] == '1':
                answer += (1<<(6-j))
        answer_list.append(answer)
    print(*answer_list)