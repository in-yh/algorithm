str = input()

palindrome = ''
for s in str:
    palindrome = s + palindrome

answer = 0
if str == palindrome:
    answer = 1

print(answer)