import sys
import heapq

def dijkstra(num):
    check[num] = True # 감염여부
    time[num] = 0 # 시간정보
    h = []
    heapq.heappush(h, (0, num))
    while h:
        pcost, now = heapq.heappop(h)
        if pcost > time[now]:
            continue
        for cost, next in info[now]:
            ncost = pcost + cost
            if time[next] > ncost:
                time[next] = ncost
                heapq.heappush(h, (ncost, next))
                check[next] = True

T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())
    info = [list() for _ in range(N+1)]
    for _ in range(D):
        A, B, S = map(int, sys.stdin.readline().split())
        info[B].append((S, A))
    
    check = [False] * (N+1) # 컴퓨터별 감염여부 저장
    time = [1e9] * (N+1) # 컴퓨터별 최소 도달시간 저장
    dijkstra(C)
    # print('check :', check) # test
    # print('time :', time) # test

    # 감염된 컴퓨터 개수 및 감염된 컴퓨터 중 가장 긴 시간 정보 저장
    result_count = 0
    result_time = 0
    for i in range(N+1):
        if check[i] == True:
            result_count += 1 # 감염된 컴퓨터 개수 +1
            if result_time < time[i]: # 가장 긴 시간 정보로 업데이트
                result_time = time[i]

    print(result_count, result_time)