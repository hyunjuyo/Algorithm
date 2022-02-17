N = int(input())
arr = list(map(int, input().split()))

info = [1] * N # 1로 초기화

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            info[i] = max(info[j] + 1, info[i]) # 가장 큰 값으로 유지

    print(info) # test

print(max(info))