import sys

def is_true(arr):
    for i in range(1, N):
        if arr[i-1] == arr[i][:len(arr[i-1])]:
            return 'NO'
    return 'YES'

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(sys.stdin.readline()[:-1])
    arr.sort()

    ret = is_true(arr)
    print(ret)