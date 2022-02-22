import sys
import heapq

INF = int(1e9)

N, M = map(int, input().split())
info = [[0, i, 0] for i in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    info[A][2] = B # 이후에 풀 문제번호 저장
    info[B][0] = A # 이전에 풀 문제번호 저장

# heap 정보 저장
heap_list = []
for i, v in enumerate(info):
    if i > 0 and v[0] == 0:
        heapq.heappush(heap_list, [v[1], v[2]])

print(info) # test
print(heap_list) # test

result = []
while heap_list:
    print(heap_list) # test
    now, after = heapq.heappop(heap_list)
    print(f'now : {now}, after : {after}') # test
    result.append(now) # 결과 리스트에 순서대로 저장
    after_now, after_after = info[after][1], info[after][2]
    if after != 0 and [after_now, after_after] not in heap_list:
        heapq.heappush(heap_list, [after_now, after_after])
    # info[after][0] = 0 # 이후에 풀 문제번호 index로 가서 해당 index의 이전에 풀 문제번호 0으로 바꾸기

print(*result)