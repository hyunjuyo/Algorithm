import sys
INF = sys.maxsize

def get_max_length(sorted_arr):
    max_length = sorted_arr[0] # 첫 휴게소까지의 거리로 초기화
    idx = 0
    for i in range(1, len(sorted_arr)): # arr은 이미 정렬된 상태
        if sorted_arr[i] - sorted_arr[i-1] > max_length:
            max_length = sorted_arr[i] - sorted_arr[i-1]
            idx = i
    if L - sorted_arr[-1] > max_length:
        max_length = L - sorted_arr[-1]
        idx = L
    return max_length, idx

N, M, L = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

for n in range(1, M+1):
    print(n, '-'*50) # test
    max_len, idx = get_max_length(pos)
    print('max_len, idx :', max_len, idx) # test
    new_len = max_len // 2
    pos.insert(idx, pos[idx] - new_len)
    print(pos) # test

max_len, idx = get_max_length(pos)
print(max_len)