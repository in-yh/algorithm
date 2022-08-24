# 연습문제1_큐 구현
# 2022-08-24

queue = [0]*10
front = -1
rear = -1

rear += 1 # enqueue(1)
queue[rear] = 1

rear += 1
queue[rear] = 2

rear += 1
queue[rear] = 3

front += 1 # dequeue()
print(queue[front])

front += 1
print(queue[front])

front += 1
print(queue[front])