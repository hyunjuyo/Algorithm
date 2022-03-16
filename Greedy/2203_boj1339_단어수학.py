from collections import defaultdict

def get_alphabet_score(arr):
    score_dict = defaultdict(list)
    for word in arr:
        lth = len(word) - 1
        for w in word:
            score_dict[w].append(10**lth) # 자리수 크기 저장
            lth -= 1
    return score_dict

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))

# 높은 자리 순서로 점수 부여
alphabet_score = get_alphabet_score(arr)
print(alphabet_score) # test

# 점수 높은 순서로 정렬하기
info = []
for k, v in alphabet_score.items():
    info.append((sum(v), k)) # 자리수 크기 모두 더하기
info.sort(reverse=True)
print('info :', info) # test

# 알파벳 -> 숫자 대체하기
scores = "9876543210"
a_order = ''.join(list(zip(*info))[1])
replace_table = str.maketrans(a_order, scores[:len(a_order)])
result = []
for v in arr:
    result.append(int(''.join(v).translate(replace_table)))

print('result : ', result) # test
print(sum(result))