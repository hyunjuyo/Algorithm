N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = [False] * N
for i in range(N):
    l = 1 if i == 0 else 0
    r = N-2 if i == N-1 else N-1

    while l < r:
        sum_num = arr[l] + arr[r]
        if sum_num == arr[i]:
            result[i] = True
            break
        elif sum_num > arr[i]:
            r -= 1
            if r == i:
                r -= 1
        else:
            l += 1
            if l == i:
                l += 1
    
    print(arr[i], '=>', arr[l], arr[r], result) # test

print(sum(result))