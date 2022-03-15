from collections import deque

N, M = map(int, input().split())
info = [[0, 0, i] for i in range(N+1)]
left = [list() for _ in range(N+1)]
right = [list() for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    info[A][1] += 1 # 뒤에 있는 학생수 +1
    info[B][0] += 1 # 앞에 있는 학생수 +1
    left[B].append(A)
    right[A].append(B)

info.pop(0)
info.sort(key=lambda x:(x[0], -x[1]))

start = []
for v in info:
    if v[0] != 0:
        break
    start.append(v[2])

print(info) # test
print(start) #test

index = [-1] * (N+1)
idx = 0
result = []
q = deque([start[0]])
while q:
    now = q.popleft()
    result.append(now)
    index[now] = idx
    idx += 1
    for next in right[now]:
        q.append(next)
        break

print(result) # test
print(index) # test

insert_info = []
for num in range(1, N+1):
    if index[num] == -1:
        print(num, left[num]) # test
        max_idx = 0
        for v in left[num]:
            print('v :', v, 'index[v] :', index[v]) # test
            max_idx = max(max_idx, index[v] + 1)
        insert_info.append((max_idx, num))

insert_info.sort(reverse=True, key=lambda x:x[0])
for v in insert_info:
    result.insert(v[0], v[1])

print(result)