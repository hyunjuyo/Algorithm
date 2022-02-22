import sys
import heapq

N, M = map(int, input().split())
info = [[0, i, []] for i in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    info[A][2].append(B) # 이후에 풀 문제번호 리스트 저장
    info[B][0] += 1 # 이전에 풀 문제개수 +1

# heap 정보 저장
heap_list = []
for i, v in enumerate(info):
    if i > 0 and v[0] == 0: # 이전에 풀 문제개수가 0인 경우
        heapq.heappush(heap_list, [v[1], v[2]])

print('info :', info) # test

result = []
while heap_list:
    print('\nheap_list :', heap_list, '\n') # test
    now, after_list = heapq.heappop(heap_list)
    print('-'*20, f'now : {now}, after : {after_list}', '-'*20) # test
    result.append(now) # 결과 리스트에 순서대로 저장
    for after in after_list:
        after_now, after_after = info[after][1], info[after][2]
        if [after_now, after_after] not in heap_list:
            heapq.heappush(heap_list, [after_now, after_after])
        # info[after][0] = 0 # 이후에 풀 문제번호 index로 가서 해당 index의 이전에 풀 문제번호 0으로 바꾸기

print(*result)