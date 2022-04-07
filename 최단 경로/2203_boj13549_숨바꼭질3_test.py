from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001 # 방문여부 기록용

q = deque([(N, 0)]) # 위치, 시간
result = 0
while q:
    now, sec = q.popleft()
    visited[now] = True # 방문 기록
    if 0 <= now - 1 <= 100000:
        if now - 1 == K:
            result = sec + 1
            break
        elif visited[now - 1] is False: # 최초 방문 시
            q.append((now - 1, sec + 1))
    if 0 <= now + 1 <= 100000:
        if now + 1 == K:
            result = sec + 1
            break
        elif visited[now + 1] is False: # 최초 방문 시
            q.append((now + 1, sec + 1))
    if 0 <= now * 2 <= 100000:
        if now * 2 == K:
            result = sec
            break
        elif visited[now * 2] is False: # 최초 방문 시
            q.append((now * 2, sec))
    
    print(q) # test

print(result)