def check(mid):
    total = 0
    for i in range(len(arr)):
        if mid < arr[i]:
            total += mid
        else:
            total += arr[i]
    
    if total <= M:
        return True
    else:
        return False

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

result = 0
l = 1
r = max(arr)
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        result = max(result, mid)
        l = mid + 1
    else:
        r = mid - 1

print(result)