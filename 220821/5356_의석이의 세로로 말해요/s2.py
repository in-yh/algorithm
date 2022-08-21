# 5356_의석이의 세로로 말해요
# 2022-08-21

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    string = ['']*15

    for _ in range(5):
        words = input()
        for idx, word in enumerate(words):
            string[idx] += word

    result = ''
    for s in string:
        result += s

    print('#{} {}'. format(tc, result))