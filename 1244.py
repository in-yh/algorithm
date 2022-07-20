switch_num = int(input())
switch_status = list(map(int, input().split()))
student = int(input())
student_sex = list(range(student))
student_num = list(range(student))
i = 0

while i < student:
    student_sex[i], student_num[i] = map(int, input().split())
    i += 1

i = 0
j = 1
k = 1
for i in range(student):
    if student_sex[i] == 1:
        while student_num[i] * j <= switch_num:
            if switch_status[student_num[i] * j] == 0:
                switch_status[student_num[i] * j] = 1
            else:   
                switch_status[student_num[i] * j] = 0
            j += 1   
    else:
        while 1 <= student_num[i-k] <= switch_num | student_num[i+k]:
            if student_num[i-k] == student_num[i+k]:
                student_num