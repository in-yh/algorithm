# 연습문제2_정수를 문자열로 반환
# 2022-08-12

def itoa(number):
    # 0이면 '0'
    if number == 0:
        return '0'

    # 양수, 음수 체크
    if number < 0:
        flag = False
        number = -(number)
    else:
        flag = True

    # 하나씩 쪼개서 더해줌
    result = ''
    # 10씩 쪼개서 나머지를 하나하나 결과값에 더해준다.
    while number: # 1234
        number, remainder = number//10, number%10 # 값, 나머지
        result = chr(ord('0')+remainder) + result # 맨 마지막 값부터 채워지니 result를 뒤에 더해줌

    # 음수는 다시 -붙여주기
    if flag == True:
        return result
    else:
        return '-'+(result) # 문자열이기에 더해줘야 함

print(itoa(-1234)) # -1234
print(type(itoa(-1234))) # str