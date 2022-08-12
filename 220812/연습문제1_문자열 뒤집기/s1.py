# 연습문제1_문자열 뒤집기
# 2022-08-12

s = 'algorithm' # 문자열 저장
list_s = list(s) # 문자열 리스트화

for i in range((len(list_s))//2): # 9 // 2 = 4
    list_s[i], list_s[-(i+1)] = list_s[-(i+1)], list_s[i]

s = ''.join(list_s)

print(s)