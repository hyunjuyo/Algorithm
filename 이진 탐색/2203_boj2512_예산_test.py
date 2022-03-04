def check():
    if sum(arr) <= M: # 모든 요청이 배정될 수 있는 경우
        return max(arr)

    cand = M // N # 평균금액으로 초기화
    buffer_a = M % N # 나머지 저장해놓기
    plus = 0
    minus = 0
    buffer_b = 0
    for i in range(len(arr)):
        if arr[i] < cand: # 평균금액 보다 작은 경우
            buffer_b += (cand - arr[i]) # 여유금액 저장
            plus += 1 # 개수 +1
        else:
            minus += 1 # 개수 +1

    return cand + ((buffer_b + buffer_a) // minus)

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

result = check()
print(result)