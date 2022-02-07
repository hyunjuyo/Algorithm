def get_arr_dict(N, K):
    arr_dict = {}
    if K == 0:
        arr_dict[2] = [['B', 'A']]
    else:
        arr_dict[2] = [['A', 'B']]

    for lth in range(3, N+1):
        arr_dict[lth] = []
        for arr in arr_dict[lth-1]:
            tmp_arr = arr.copy()
            tmp_arr.insert(0, 'A')
            if tmp_arr not in arr_dict[lth]:
                arr_dict[lth].append(tmp_arr)
            tmp_arr = arr.copy()
            tmp_arr.append('A')
            if tmp_arr not in arr_dict[lth]:
                arr_dict[lth].append(tmp_arr)
            tmp_arr = arr.copy()
            tmp_arr.insert(0, 'B')
            if tmp_arr not in arr_dict[lth]:
                arr_dict[lth].append(tmp_arr)
            tmp_arr = arr.copy()
            tmp_arr.append('B')
            if tmp_arr not in arr_dict[lth]:
                arr_dict[lth].append(tmp_arr)

    return arr_dict

# 문자열 내에서 조건을 만족하는 쌍의 개수 반환 함수
def get_count(arr):
    count = 0
    for i, v in enumerate(arr):
        if v == 'A':
            count += arr[i+1:].count('B')
    return count

N, K = map(int, input().split())

arr_dict = get_arr_dict(N, K)
# print(arr_dict)

S = ''
for arr in arr_dict[N]:
    print(arr) # test
    if get_count(arr) == K:
        S = ''.join(arr)
        break

if len(S) == 0:
    print(-1)
else:
    print(S)