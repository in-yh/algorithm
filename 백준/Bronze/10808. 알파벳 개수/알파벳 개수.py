in_string = input()

answer = [0]*26

for s in in_string:
    answer[ord(s)-ord('a')] += 1

print(*answer)