from collections import deque

def check(q):
    global result

    while q:
        v_list = q.popleft()
        # print('v_list :', v_list) # test
        m_sum = 0
        c_sum = 0
        for v in v_list:
            m_sum += v[0]
            c_sum += v[1]
        if m_sum >= M:
            result = min(result, c_sum)
    
    return q

N, M = map(int, input().split())
m_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

info = [[0, 0] for _ in range(N+1)]
for i in range(1, N+1):
    info[i][0] = m_list[i-1]
    info[i][1] = c_list[i-1]
info.sort()

result = int(1e9)

i = 1
q = deque()
q.append([(0, 0)])
q.append([tuple(info[i])])
while q:
    tmp_list = list(q)
    check(q)
    
    if i < N:
        i += 1
        for tmp in tmp_list:
            tmp_copy = tmp[:]
            tmp_copy.append((0, 0))
            q.append(tmp_copy)
            tmp_copy = tmp[:]
            tmp_copy.append(tuple(info[i]))
            q.append(tmp_copy)

    print(q) # test

print(result)