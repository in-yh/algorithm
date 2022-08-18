# 연습문제1_스택구현
# 2022-08-17

stack = [0]*3 # 사이즈 먼저 설정해줘야 함
top = -1 # top 초기값을 지하(-1)로 설정

top += 1
stack[top] = 1

top += 1
stack[top] = 2

top += 1
stack[top] = 3

top -= 1
data = stack[top+1]
print(data)

top -= 1
data = stack[top+1]
print(data)

top -= 1
data = stack[top+1]
print(data)