from collections import deque

A, B = map(int, input().split())

flag = False
result = 0
q = deque([[A, 1]])
while q:
    now, count = q.popleft()
    if now == B:
        flag = True
        result = count
    if now < B:
        q.append([now*2, count+1])
        q.append([int(str(now)+'1'), count+1])
    
    # print(q) # test

if flag == True:
    print(result)
else:
    print(-1)