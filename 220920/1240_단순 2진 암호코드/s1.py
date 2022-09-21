# 1240_단순 2진 암호코드
# 2022-09-20

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    password = [input() for _ in range(N)]

    # 암호코드 정보 추출 : 1이 나오는 줄 찾고, 뒤부터 순회해서 1이 나오는 곳부터 56개 추출
    for i in range(N): 
        if '1' in password[i]:
            password = password[i]
            break
    
    for j in range(M-1, -1, -1):
        if password[j] == '1':
            final_index = j
            break
    password = password[final_index-55:final_index+1]

    # 7개씩 끊은 후 어떤 수와 매치되는지 찾기
    code = {'0001101' : '0', 
            '0011001' : '1',
            '0010011' : '2',
            '0111101' : '3',
            '0100011' : '4',
            '0110001' : '5',
            '0101111' : '6',
            '0111011' : '7',
            '0110111' : '8',
            '0001011' : '9',
        }

    result = []
    for k in range(0, len(password), 7):
        result.append(code[password[k:k+7]])
    
    # (홀수자리의합*3 + 짝수자리의합)이 10의 배수가 되는지 확인
    sum1 = 0
    sum2 = 0
    for l in range(8):
        if l%2:
            sum2 += int(result[l])
        else: # 짝수
            sum1 += int(result[l])

    if (sum1*3 + sum2) % 10 == 0:
        answer = sum1 + sum2
    else:
        answer = 0

    print('#{} {}'.format(tc, answer))