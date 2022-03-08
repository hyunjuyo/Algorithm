N, M = map(int, input().split())
m_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

max_cost = sum(c_list)
table = [[0] * max_cost for _ in range(N)]

result = sum(c_list)
for i in range(N):
    for j in range(max_cost):
        memory = m_list[i]
        cost = c_list[i]
        if cost <= j:
            table[i][j] = max(memory + table[i-1][j-cost], table[i-1][j])
        else:
            table[i][j] = table[i-1][j]
        
        if table[i][j] >= M:
            result = min(result, j)

for v in table:
    print(v)

print(result)