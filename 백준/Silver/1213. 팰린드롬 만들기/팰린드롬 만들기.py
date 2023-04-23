import sys
import collections

word = sys.stdin.readline().rstrip()
check_word = collections.Counter(word)
cnt = 0
mid = ''
answer = ''
for k, v in list(check_word.items()):
    if v%2 == 1:
        cnt += 1
        mid = k
        if cnt > 1:
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_word.items()):
    answer += k*(v//2)

print(answer + mid + answer[::-1])