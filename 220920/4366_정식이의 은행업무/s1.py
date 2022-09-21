# 4366_정식이의 은행업무
# 2022-09-20

import sys
sys.stdin = open('input.txt', 'r')

# 2진수, 3진수 -> 10진수
def change_decimal(memory, n):
    answer = 0
    for i in range(len(memory)):
        answer += int(memory[i])*(n**(len(memory)-1-i))
    return answer

# 2진수를 1자리씩 고쳐서 후보 리스트 만듦
def candidate_2(memory):
    decimal_2 = change_decimal(memory, 2) # 2진수를 10진수로 바꿔준 값, 10
    candidate_2_list = []
    for idx, k in enumerate(memory):
        if k == '0':
            value = decimal_2 + 2**(len(memory)-1-idx) 
        else:
            value = decimal_2 - 2**(len(memory)-1-idx)
        candidate_2_list.append(value)
    return candidate_2_list

# 3진수를 1자리씩 고쳐서 후보 리스트 만듦
def candidate_3(memory):
    decimal_3 = change_decimal(memory, 3) # 3진수를 10진수로 바꿔준 값, 23
    candidate_3_list = []
    for idx, k in enumerate(memory):
        if k == '0':
            value1 = decimal_3 + 3**(len(memory)-1-idx)
            value2 = decimal_3 + 2*(3**(len(memory)-1-idx))
        elif k == '1':
            value1 = decimal_3 + 3**(len(memory)-1-idx)
            value2 = decimal_3 - 3**(len(memory)-1-idx)
        else:
            value1 = decimal_3 - 3**(len(memory)-1-idx)
            value2 = decimal_3 - 2*(3**(len(memory)-1-idx))
        candidate_3_list.append(value1)
        candidate_3_list.append(value2)
    return candidate_3_list

T = int(input())
for tc in range(1, T+1):
    memory_2 = input() # '1010'
    memory_3 = input() # '212'

    for c in candidate_2(memory_2):
        if c in candidate_3(memory_3):
            result = c
            break
    
    print('#{} {}'. format(tc, result))

'''
'1010'을 순회 
0이면 +2^i 후 리스트 저장
1이면 -2^i 후 리스트 저장

'212'을 순회
0이면 +3^i 와 +2*3^i 각각 수행 후 리스트 저장
1이면 +3^i 와 -3^i 각각 수행 후 리스트 저장
2이면 -3^i 와 -2*3^i 각각 수행 후 리스트 저장

각각의 리스트에서 공통된 것 찾기
'''