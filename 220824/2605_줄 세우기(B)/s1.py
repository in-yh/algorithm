# 2605_줄 세우기(B)
# 2022-08-25

import sys
sys.stdin = open('input.txt', 'r')

student_number = int(input()) # 학생 수

stack = []
temp = []
L = list(map(int, input().split())) # 학생이 뽑은 번호

for i in range(student_number): # 학생 수만큼 반복
    if L[i] == 0: # 학생이 뽑은 번호가 0이면 stack에 추가
        stack.append(i+1)
    else:
        for j in range(100): # 학생이 뽑은 번호가 0~99까지 가능
            if L[i] == j: # 학생이 뽑은 번호가 j라면
                for _ in range(j): # j만큼 stack에서 pop한 후 temp에 push
                    temp.append(stack.pop())
                stack.append(i+1) # pop 다 한 후에 본인을 stack에 push
                for _ in range(j): # j만큼 temp에서 pop한 후 stack에 push
                    stack.append(temp.pop())  
print(*stack) # 리스트화로 말고!!

        
