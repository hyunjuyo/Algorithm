import sys
INF = int(1e9)

def get_count(mid):
    tmp_total = [row[:] for row in total] # 복사본 생성
    count = 0
    for arr in tmp_total:
        i = 1
        while arr[-1] < mid:
            i += 1
            if arr[0] * i <= mid:
                arr.append(arr[0] * i)
            else:
                i -= 1
                break
        count += i
    for v in tmp_total: # test
        print(v)
    print('-'*30) # test
    v_list = []
    for v in tmp_total:
        v_list.extend(v)
    return count, v_list

N, M = map(int, input().split())
# 2차원 배열로 초기화
total = []
max_num = 0
for _ in range(N):
    time = int(sys.stdin.readline())
    total.append([time]) # 각 배열의 첫번째 값으로 초기화
    if max_num < time: # 가장 큰 값 저장
        max_num = time

result = []
l = 1
r = max_num * M
while l <= r:
    mid = (l + r) // 2
    print(mid) # test
    count, v_list = get_count(mid)
    print('count :', count) # test
    print('v_list :', v_list) # test

    if count >= M:
        result = v_list
        r = mid - 1
    else:
        l = mid + 1

    print(sorted(result)) # test

result.sort()
print(result[M-1])