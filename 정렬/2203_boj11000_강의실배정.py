import sys
import heapq

N = int(input())
arr = []
for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    arr.append((S, T))

arr.sort()

heap_list = []
heapq.heappush(heap_list, arr[0][1]) # 첫번째 강의 끝나는 시간으로 초기화
for i in range(1, len(arr)):
    if arr[i][0] < heap_list[0]: # 배정된 강의 중 가장 빨리 끝나는 시간 보다 일찍 시작하는 경우
        heapq.heappush(heap_list, arr[i][1])
    else:
        heapq.heappop(heap_list) # 업데이트를 위해 기존 데이터 없애기
        heapq.heappush(heap_list, arr[i][1]) # 현재 강의가 끝나는 시간으로 업데이트

    # print(heap_list) # test

print(len(heap_list))