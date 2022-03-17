N = int(input())
max_day = 0
info = [list() for _ in range(1000+1)]
for _ in range(N):
    D, W = map(int, input().split())
    info[D].append(W)
    max_day = max(max_day, D)

# print(info) # test

result = []
tmp = [] # 임시 저장 리스트
minus = 0
for d in range(1, max_day+1):
    print('-'*20, 'd :', d) # test
    tmp.extend(info[d]) # 임시 저장
    print('tmp :', tmp) # test
    if len(tmp) > d: # 일수보다 과제수가 더 많아질 경우
        tmp.sort(reverse=True)
        result.extend(tmp[:d - minus]) # 과제 점수 높은 순서로 결과 저장
        tmp = [0] * d # 임시 저장 리스트에 개수만 채우기
        minus = d
        print('result :', result) # test

# 임시 저장 리스트에 남아있는 과제 점수 더하기
tmp.sort(reverse=True)
for v in tmp:
    if v > 0:
        result.append(v)

print(result) # test
print(sum(result))