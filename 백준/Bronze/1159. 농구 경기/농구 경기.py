i = int(input())

alphabet = [0]*26
for _ in range(i):
    str = input()
    alphabet[ord(str[0])-ord("a")] += 1

answer = []
for idx, alpha in enumerate(alphabet):
    if alpha >= 5:
        answer.append(chr(idx+97))

if answer == []:
    print("PREDAJA")
else:
    sorted(answer)
    answer = ''.join(answer)
    print(answer)