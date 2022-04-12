from collections import deque

N = int(input())

inDegree = [0] * (N+1)
info = [list() for _ in range(N+1)]
cost_list = [0] * (N+1)
for i in range(1, N+1):
    input_v = list(map(int, input().split()))
    cost, n, tmp = input_v[0], input_v[1], input_v[2:]

    cost_list[i] = cost # 작업 소요시간 저장
    inDegree[i] = n # 선행해야 할 작업 개수 저장
    for v in tmp: # 이후 작업 가능한 작업번호 저장
        info[v].append(i)

print('inDegree :', inDegree) # test
print('info :', info) # test
print('cost_list:', cost_list) # test

max_cost = [0] * (N+1) # 선행작업 누적시간 중 최대값 저장용
q = deque()
for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append((i, 0))
while q:
    now, cost = q.popleft()
    print('now, cost :', now, cost) # test
    cost += cost_list[now]
    print(cost_list[now], 'after cost :', cost) # test
    for next in info[now]:
        print('next :', next) # test
        max_cost[next] = max(max_cost[next], cost) # 선행작업 누적시간 중 최대값으로 업데이트
        inDegree[next] -= 1 # 선행작업 개수 -1
        if inDegree[next] == 0:
            q.append((next, max_cost[next]))
    print(q) # test
    print('-'*50) # test

print('max_cost :', max_cost) # test
print(cost)