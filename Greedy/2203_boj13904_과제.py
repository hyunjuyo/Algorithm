N = int(input())
max_day = 0
info = [list() for _ in range(1000+1)]
for _ in range(N):
    D, W = map(int, input().split())
    info[D].append(W)
    max_day = max(max_day, D)

# print(info) # test

result = []
for d in range(1, max_day+1):
    print('-'*20, 'd :', d) # test
    result.extend(info[d])
    print('result1 :', result) # test
    if len(result) > d: # 일수보다 과제수가 더 많아질 경우
        result.sort(reverse=True)
        result = result[:d] # 과제 점수 높은 순서로 가능한 과제수 개수만큼 저장
        print('result2 :', result) # test

print(result) # test
print(sum(result))