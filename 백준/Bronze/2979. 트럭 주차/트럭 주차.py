A, B, C = map(int, input().split())

time = [0]*100 # 0~99
for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        time[i] += 1

answer = 0
for t in time:
    if t == 3:
        answer += 3*C
    elif t == 2:
        answer += 2*B
    elif t == 1:
        answer += A

print(answer)