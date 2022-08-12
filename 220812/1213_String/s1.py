# 1213_String
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def BruteForce(pattern, text):
    cnt = 0
    # text를 처음부터 끝까지 순회하면서(단, pattern의 길이에 맞게)
    for i in range(len(text) - len(pattern) + 1):
        # pattern을 처음부터 끝까지 순회하면서
        for j in range(len(pattern)):
            # 다르면 break
            if text[i+j] != pattern[j]: # 위로 올라가 그 다음 i로 간다
                break # 여기가 break이면 아래 else문 실행되지 않고 그 아래 else문은 실행됨.
        # 다른게 없다면 정답이므로, i(시작점) return
        else:
            cnt += 1
    else: # 위에서 완전탐색을 해도 답을 찾지 못한다면 이 else문 실행됨
        pass # 여기에 cnt = 0하면 초기화됨 
    
    return cnt

for _ in range(10):
    tc = int(input())
    search_str = input() # 찾을 패턴
    origin_str = input() # 전체 텍스트

    result = BruteForce(search_str, origin_str)

    print('#{} {}'. format(tc, result))