import heapq

def dijkstra(n):
    lth_list[n] = 0
    h = []
    heapq.heappush(h, (0, n))
    while h:
        pcost, now = heapq.heappop(h)
        if pcost > lth_list[now]:
            continue
        for c, i in info[now]:
            ncost = pcost + c
            if lth_list[i] > ncost:
                lth_list[i] = ncost
                heapq.heappush(h, (ncost, i))

N, M, R = map(int, input().split())
item_list = list(map(int, input().split()))
item_list.insert(0, 0) # index 0 추가
info = [list() for _ in range(N+1)]
for _ in range(R):
    a, b, lth = map(int, input().split())
    info[a].append((lth, b))
    info[b].append((lth, a))

print(item_list) # test
for v in info: # test
    print(v)

# 각 지역에 떨어지는 케이스별 최대 아이템 개수 확인
count_list = []
for n in range(1, N+1):
    # 시작지점 기준 최단거리 정보 저장
    lth_list = [1e9] * (N+1)
    dijkstra(n)
    print(lth_list) # test

    count = 0
    for i in range(N+1):
        if lth_list[i] <= M:
            count += item_list[i]
    count_list.append(count)
    print(count_list) # test

print(max(count_list))