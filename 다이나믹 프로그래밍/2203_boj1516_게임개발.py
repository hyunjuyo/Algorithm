from collections import deque

N = int(input())
inDegree = [0] * (N+1)
time = [0] * (N+1)
info = [list() for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()[:-1]))
    time[i] = tmp.pop(0)
    for v in tmp:
        inDegree[i] += 1
        info[v].append(i)

print("inDegree :", inDegree)
print('time :', time)
print('info :', info)

result = [0] * (N+1)
q = deque([])
for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    result[now] += time[now]
    for v in info[now]:
        inDegree[v] -= 1
        if inDegree[v] == 0:
            q.append(v)

print("inDegree :", inDegree)
print('time :', time)
print('info :', info)
print(result)