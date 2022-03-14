def dfs(y, x):
    tmp_table[y][x] = -1 # 확인된 지점 -1 입력

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서
    for i in range(4):
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if tmp_table[ny][nx] > 0:
            dfs(ny, nx)

def get_count(tmp_table):
    count = 0
    for i in range(N):
        for j in range(N):
            if tmp_table[i][j] > 0:
                dfs(i, j)
                count += 1
    return count

N = int(input())
table = []
h = 0 # 가장 높은값 저장 변수
l = 101 # 가장 낮은값 저장 변수
for _ in range(N):
    tmp = list(map(int, input().split()))
    table.append(tmp)
    h = max(h, max(tmp)) # 가장 높은값 저장
    l = min(l, min(tmp)) # 가장 낮은값 저장
# print(h, l) # test

result = []
for height in range(l, h+1):
    tmp_table = [row[:] for row in table] # 복사본 생성
    for i in range(N):
        for j in range(N):
            if tmp_table[i][j] <= height: # 해당 높이 이하일 경우
                tmp_table[i][j] = 0
    print('height :', height) # test
    for v in tmp_table: # test
        print(v)

    count = get_count(tmp_table)
    result.append(count)
    print('count :', count) # test
    print('-'*30) # test

print(result) # test
print(max(result))