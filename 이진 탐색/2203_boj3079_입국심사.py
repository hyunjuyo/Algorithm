import sys
# INF = int(1e9)

def get_total_count(mid):
    tmp_count = [v for v in count] # 복사본 생성
    print('time :', time) # test
    for i in range(N):
        tmp_count[i] = mid // time[i] # 가능한 횟수 저장
    print('count :', tmp_count) # test

    return sum(tmp_count)

N, M = map(int, input().split())

time = []
max_num = 0
for _ in range(N):
    v = int(sys.stdin.readline())
    time.append(v)
    if max_num < v: # 가장 큰 값 저장
        max_num = v
count = [0] * N

result = max_num * M + 1 # 최대값 설정 -> 1e9 보다 큰 숫자임 !!!!!
l = 1
r = max_num * M
while l <= r:
    mid = (l + r) // 2
    print('mid :', mid) # test
    total_count = get_total_count(mid)

    if total_count >= M:
        result = min(result, mid)
        print('result 저장 ==================>', result) # test
        r = mid - 1
    else:
        l = mid + 1
    
    print('total_count :', total_count) # test
    print('-'*50)  # test

print(result)