import math

INF = math.inf

# 벨만 포드(bellman_ford)
def bf(s):
    time[s] = 0 # 시작지점 시간 0
    for i in range(N):
        for j in range(M):
            now = info[j][0]
            next = info[j][1]
            dt = info[j][2]
            if time[now] != INF and time[next] > time[now] + dt:
                time[next] = time[now] + dt
                if i == N - 1:
                    return False
    return True
                    
N, M = map(int, input().split())

info = []
for _ in range(M):
    a, b, c = map(int, input().split())
    info.append((a, b, c))

time = [INF] * (N+1)
flag = bf(1)

if flag:
    for v in time[2:]:
        if v == INF:
            print(-1)
        else:
            print(v)
else:
    print(-1)