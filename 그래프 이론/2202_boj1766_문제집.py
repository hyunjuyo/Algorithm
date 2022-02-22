import sys
import heapq

N, M = map(int, input().split())
before_info = [0] * (N+1)
after_info = [[] for i in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    after_info[A].append(B) # 이후에 풀 문제번호 리스트 저장
    before_info[B] += 1 # 이전에 풀 문제개수 +1

# heap 정보 저장
heap_list = []
for i, v in enumerate(before_info):
    if i > 0 and v == 0: # 이전에 풀 문제개수가 0인 경우
        heapq.heappush(heap_list, i)

result = []
while heap_list:
    # print('\nheap_list :', heap_list, '\n') # test
    now = heapq.heappop(heap_list)
    # print('-'*20, f'now : {now}, after : {after_info[now]}', '-'*20) # test
    result.append(now) # 결과 리스트에 순서대로 저장
    for after in after_info[now]:
        before_info[after] -= 1 # 이전에 풀 문제개수 -1
        if before_info[after] == 0:
            heapq.heappush(heap_list, after)

print(*result)