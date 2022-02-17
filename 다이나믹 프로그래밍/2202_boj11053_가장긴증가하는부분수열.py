

N = int(input())
arr = list(map(int, input().split()))

info = []
for i, v1 in enumerate(arr):
    count = 1
    tmp = v1
    for j, v2 in enumerate(arr):
        if i < j and tmp < v2: # 시작 index 다음부터 값이 증가할 때마다 업데이트
            count += 1
            tmp = v2
    info.append(count)

print(info) # test
print(max(info))