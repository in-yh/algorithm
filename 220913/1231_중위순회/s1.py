# 1231_중위순회
# 2022-09-13

import sys
sys.stdin = open('input.txt', 'r')

def in_order(n):
    global answer
    if n:
        in_order(ch1[n])
        answer.append(words[n])
        in_order(ch2[n])
    return answer

for tc in range(1, 11):
    N = int(input()) # 정점 개수
    words = [0]*(N+1) # W F R O T A E S 를 넣을 리스트
    # 부모 인덱스로 자식을 리스트에 넣기
    ch1 = [0]*(N+1) # 왼쪽자식
    ch2 = [0]*(N+1) # 오른쪽자식 
    for _ in range(N):
        input_list = list(input().split())
        if len(input_list) == 4:
            num, alphabet, L, R = input_list
            num, L, R = int(num), int(L), int(R)
            ch1[num] = L
            ch2[num] = R 
        elif len(input_list) == 3:
            num, alphabet, L = input_list
            num, L = int(num), int(L)
            ch1[num] = L
        elif len(input_list) == 2:
            num, alphabet = input_list
            num = int(num)
        
        words[num] = alphabet
    
    # 중위순회하기
    answer = []
    in_order(1) # 루트는 항상 1

    # ['S', 'O', 'F', 'T', 'W', 'A', 'R', 'E'] -> SOFTWARE / '구분자'.join(리스트)
    answer = ''.join(answer) 
    print('#{} {}'. format(tc, answer))