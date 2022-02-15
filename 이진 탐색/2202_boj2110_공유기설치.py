import sys

# 주어진 dist 기준의 공유기 개수 반환 함수
def get_c_count(dist):
    c_count = 1
    tmp_num = arr[0] # 배열의 첫번째 값으로 초기화
    for i, v in enumerate(arr):
        if v - tmp_num >= dist: # dist 이상인 경우
            c_count += 1
            tmp_num = v # 업데이트
    
    return c_count

N, C = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]

arr.sort()

l = 1 # 가능한 최소값
r = arr[-1] - arr[0] # 가능한 최대값

result = 0 # 가장 작은 값으로 초기화
while l <= r:
    mid = (l + r) // 2
    c_count = get_c_count(mid)

    if c_count < C:
        r = mid - 1
    else:
        result = max(result, mid)
        l = mid + 1

print(result)