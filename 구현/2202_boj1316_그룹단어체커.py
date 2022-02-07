# ---------------------------------------------
# # 그룹단어 판단
# 1. 단어 내 연속된 문자별로 하나씩만 남기기
#   (예시) 'aabbcccb' -> ['a', 'b', 'c', 'b']
# 2. 해당 단어 내 문자별 개수가 1개를 초과하는지 여부 체크
# ---------------------------------------------

# 그룹단어 여부 확인 함수
def is_group_word(s):
    ret = True

    # 연속된 문자별로 하나씩만 남기기
    unique_list = []
    for i, c in enumerate(s):
        if i == 0 or s[i - 1] != c:
            unique_list.append(c)

    # 리스트 내 원소의 개수가 2개 이상인 경우 False
    for c in unique_list:
        if unique_list.count(c) > 1:
            ret = False
            break

    return ret

N = int(input()) # 단어 개수 입력

word_list = []
for _ in range(N):
    word_list.append(input()) # N개 단어 입력

count = 0
for s in word_list:
    if is_group_word(s): # 그룹단어일 경우, count 증가
        count += 1

print(count)