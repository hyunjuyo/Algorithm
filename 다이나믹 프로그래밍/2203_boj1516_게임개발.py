from collections import deque

N = int(input())
inDegree = [0] * (N+1)
time = [0] * (N+1)
l = [list() for _ in range(N+1)]
r = [list() for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()[:-1]))
    time[i] = tmp.pop(0)
    for v in tmp:
        inDegree[i] += 1
        l[i].append(v)
        r[v].append(i)

print("inDegree :", inDegree)
print('time :', time)

result = [0] * (N+1)
q = deque([])
for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    result[now] += time[now]
    for v in r[now]:
        inDegree[v] -= 1
        result[v] += result[now]
        if inDegree[v] == 0:
            q.append(v)

print("inDegree :", inDegree)
print('time :', time)
print(l)
print(r)
print(result)
