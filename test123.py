print(1<<0)
print(1<<1)
print(1<<2)

def spring():
    for r, c in tree_list:
        tmp_list = []
        while tb_tree[r][c]:
            age = tb_tree[r][c].pop()
            tb_base[r][c] -= age
            if tb_base[r][c] < 0:
                tb_base[r][c] += age
                tree_to_food.append((age // 2, r, c))
                continue
            tmp_list.append(age + 1)
            if (age + 1) % 5 == 0:
                tree_to_grow.append((age + 1, r, c))
        tb_tree[r][c] = tmp_list

def summer():
    for food, r, c in tree_to_food:
        tb_base[r][c] += food

def fall():
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for age, r, c in tree_to_grow:
        for i in range(8):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            if nr < 1 or nr > N or nc < 1 or nc > N:
                continue
            tb_tree[nr][nc].append(1)
            if (nr, nc) not in tree_list:
                tree_list.append((nr, nc))

def winter():
    for i in range(1, N+1):
        for j in range(1, N+1):
            tb_base[i][j] += tb_food[i][j]

def get_tree_count(tb_tree):
    tree_count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            tree_count += len(tb_tree[i][j])
    return tree_count

N, M, K = map(int, input().split())
tb_tree = [[0] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        tb_tree[i][j] = []
tb_base = [[5] * (N+1) for _ in range(N+1)]
tb_food = [[0] * (N+1)]

for _ in range(N):
    tmp = list(map(int, input().split()))
    tmp.insert(0, 0)
    tb_food.append(tmp)

tree_list = []
for _ in range(M):
    X, Y, Z = map(int, input().split())
    tb_tree[X][Y].append(Z)
    if (X, Y) not in tree_list:
        tree_list.append((X, Y))

for r, c in tree_list:
    tb_tree[r][c].sort(reverse=True)

year_count = 0
while True:
    year_count += 1
    tree_to_food = []
    tree_to_grow = []
    spring()
    summer()
    fall()
    winter()
    if year_count == K:
        break

tree_count = get_tree_count(tb_tree)
print(tree_count)