import sys
INF = sys.maxsize

def get_max_length(sorted_arr):
    if len(sorted_arr) == 0:
        return L
    max_length = sorted_arr[0] # 첫 휴게소까지의 거리로 초기화
    for i in range(1, len(sorted_arr)): # arr은 이미 정렬된 상태
        if sorted_arr[i] - sorted_arr[i-1] > max_length:
            max_length = sorted_arr[i] - sorted_arr[i-1]
    if L - sorted_arr[-1] > max_length:
        max_length = L - sorted_arr[-1]
    return max_length

def add_spots(arr, mid):
    tmp_arr = arr[:]
    tmp_arr.insert(0, 0)
    tmp_arr.append(L)
    count = 0
    i = 0
    while True:
        i += 1
        if i == len(tmp_arr):
            break
        if tmp_arr[i] - tmp_arr[i-1] > mid:
            tmp_arr.insert(i, tmp_arr[i-1] + mid)
            count += 1
    tmp_arr.pop(0)
    tmp_arr.pop()
    return tmp_arr, count

N, M, L = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

result = INF
max_len = get_max_length(pos)
l = 1
r = max_len
while l <= r:
    mid = (l + r) // 2
    print('mid :', mid, '-'*50) # test

    tmp_arr, count = add_spots(pos, mid)
    print(tmp_arr, count) # test

    if count <= M:
        result = min(result, mid)
        r = mid - 1
    else:
        l = mid + 1

print(result)