# 문자열 내에서 조건을 만족하는 쌍의 개수 반환 함수
def get_count(arr):
    count = 0
    for i, v in enumerate(arr):
        if v == 'A':
            count += arr[i+1:].count('B')
    return count

N, K = map(int, input().split())

max_count = (N - (N // 2)) * (N // 2)

if K > max_count:
    print(-1)
else:
    S = ''
    arr = ['A'] * N # all 'A'로 초기화
    for i in range(1, N // 2 + 1):
        if K > (N - i) * i:
            continue
        for idx in range(i-1): # 뒤에서부터 i-1개 만큼 'B'로 채우기
            arr[-(idx+1)] = 'B'

        # print(i, arr) # test
        for idx in range(N - (i - 1)):
            tmp_arr = arr.copy()
            tmp_arr[idx] = 'B'
            # print(tmp_arr) # test
            if get_count(tmp_arr) == K:
                S = ''.join(tmp_arr)
                break
        break

    print(S)