import sys

def get_max_fuel(now_limit, stations):
    max_fuel = 0
    idx = -1
    for i in range(stations):
        if order[i][0] > now_limit: # 현재 갈 수 있는 거리보다 먼 경우
            break
        if max_fuel < order[i][1]:
            max_fuel = order[i][1]
            idx = i
    return max_fuel, idx

N = int(input())
order = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    order.append((a, b))
dist, now_limit = map(int, input().split())

print(order) # test

order.sort(key=lambda x:(x[0], -x[1])) # 가까운 순서 & 연료 양 많은 순서

count = 0
while now_limit < dist:
    print('-'*50, 'now_limit :', now_limit) # test
    print('order :', order) # test
    fuel, idx = get_max_fuel(now_limit, N-count)
    print('fuel :', fuel) # test
    if idx == -1: # 방문 가능 주유소가 없는 경우
        break
    now_limit += fuel # 연료 더하기
    order.pop(idx) # 방문한 주유소 리스트에서 제외
    count += 1 # 방문횟수 +1

if now_limit >= dist:
    print(count)
else:
    print(-1)