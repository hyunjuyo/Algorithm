from collections import deque

N, M = map(int, input().split())
info = [[0, 0, i] for i in range(N+1)]
right = [list() for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    info[B][0] += 1 # 앞에 있는 학생수 +1
    info[A][1] += 1 # 뒤에 있는 학생수 +1
    right[A].append(B) # 뒤에 있는 학생번호 저장

print(info) # test

q = deque([])
for i in range(1, N+1):
    if info[i][0] == 0:
        q.append(info[i][2])

result = []
while q:
    now = q.popleft()
    result.append(now) # 현재 번호 result 추가
    for v in right[now]:
        info[v][0] -= 1 # 진입차수 -1
        if info[v][0] == 0:
            q.append(info[v][2])

print(*result, sep=' ')