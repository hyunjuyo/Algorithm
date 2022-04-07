from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001 # 방문여부 기록용

q = deque([(N, 0)]) # 위치, 시간
visited[N] = True # 방문 기록
result = [list() for _ in range(100001)]
while q:
    now, sec = q.popleft()
    if now == K:
        result = sec
        break
    if now - 1 == K:
        result = sec + 1
        break
    elif 0 <= now - 1 <= 100000 and visited[now - 1] is False: # 최초 방문 시
        q.append((now - 1, sec + 1))
        visited[now - 1] = True # 방문 기록
    if now + 1 == K:
        result = sec + 1
        break
    elif 0 <= now + 1 <= 100000 and visited[now + 1] is False: # 최초 방문 시
        q.append((now + 1, sec + 1))
        visited[now + 1] = True # 방문 기록
    if now * 2 == K:
        result = sec
        break
    elif 0 <= now * 2 <= 100000 and visited[now * 2] is False: # 최초 방문 시
        q.appendleft((now * 2, sec))
        visited[now * 2] = True # 방문 기록
    
    print(q) # test

print(result)