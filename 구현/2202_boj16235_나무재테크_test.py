import heapq

def spring():
    # print('[spring] tree_list =>', tree_list) # test
    for r, c in tree_list:
        tmp_list = []
        # print('before :', tb_tree[r][c]) # test
        while tb_tree[r][c]:
            age = heapq.heappop(tb_tree[r][c])
            tb_base[r][c] -= age # 현재 나이만큼 양분 먹기
            if tb_base[r][c] < 0: # 땅에 양분이 부족한 경우
                tb_base[r][c] += age
                tree_to_food.append((age // 2, r, c)) # 나무->양분 정보에 추가
                continue
            tmp_list.append(age + 1) # 현재 나이 +1
            if (age + 1) % 5 == 0:
                tree_to_grow.append((age + 1, r, c)) # 나무 번식 정보에 추가
        tb_tree[r][c] = tmp_list # 나이 정보 업데이트
        # print('after :', tb_tree[r][c]) # test

def summer():
    # print('[summer] before tb_base') # test
    # for i, v in enumerate(tb_base): # test
    #     if i == 0:
    #         continue
    #     print(v[1:])

    # 나무->양분 정보 테이블에 반영
    for food, r, c in tree_to_food:
        tb_base[r][c] += food

    # print('[summer] after tb_base') # test
    # for i, v in enumerate(tb_base): # test
    #     if i == 0:
    #         continue
    #     print(v[1:])

def fall():
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # 인접한 8개 칸
    # print('[fall] tree_to_grow =>', tree_to_grow) # test
    for age, r, c in tree_to_grow:
        for i in range(8):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            if nr < 1 or nr > N or nc < 1 or nc > N: # 땅 범위를 벗어나는 경우
                continue
            heapq.heappush(tb_tree[nr][nc], 1) # 나이가 1인 나무 추가
            if (nr, nc) not in tree_list:
                tree_list.append((nr, nc))
            # print(f'heappush ({nr}, {nc})') # test
            # for tmp_r, tmp_c in tree_list: # test
            #     print(f'({tmp_r}, {tmp_c}) =>', tb_tree[tmp_r][tmp_c])
    # print('[fall] tree_list =>', tree_list) # test

def winter():
    # print('[winter] before tb_base') # test
    # for i, v in enumerate(tb_base): # test
    #     if i == 0:
    #         continue
    #     print(v[1:])

    for i in range(1, N+1):
        for j in range(1, N+1):
            tb_base[i][j] += tb_food[i][j] # 양분 추가

    # print('[winter] after tb_base') # test
    # for i, v in enumerate(tb_base): # test
    #     if i == 0:
    #         continue
    #     print(v[1:])

# 현재 기준 나무 개수 측정 함수
def get_tree_count(tb_tree):
    tree_count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            tree_count += len(tb_tree[i][j])
    
    return tree_count

N, M, K = map(int, input().split())
# tb_tree = [[[]] * (N+1) for _ in range(N+1)] # 이렇게 할 경우 메모리 공간을 서로 공유하는 케이스 발생 !!!!!
tb_tree = [[0] * (N+1) for _ in range(N+1)] # 나무 테이블
for i in range(N+1):
    for j in range(N+1):
        tb_tree[i][j] = [] # 각 위치별로 리스트로 초기화
tb_base = [[5] * (N+1) for _ in range(N+1)] # 양분 테이블
tb_food = [[0] * (N+1)] # 추가되는 양분 정보 테이블

# 추가되는 양분 정보 저장
for _ in range(N):
    tmp = list(map(int, input().split()))
    tmp.insert(0, 0) # 첫번째 열 0 추가
    tb_food.append(tmp)

tree_list = [] # 나무 위치 정보 저장용
for _ in range(M):
    X, Y, Z = map(int, input().split())
    heapq.heappush(tb_tree[X][Y], Z) # list 형태로 추가(나이 어린 순서)
    if (X, Y) not in tree_list: # 나무 위치 정보 저장
        tree_list.append((X, Y))

# for v in tb_tree: # test
#     print(v)

year_count = 0
while True:
    year_count += 1

    tree_to_food = [] # 나무->양분 list
    tree_to_grow = [] # 나무 번식 list
    spring()
    summer()
    fall()
    winter()

    print('Year', year_count, '-'*50) # test
    for i in range(1, N+1): # test
        for j in range(1, N+1):
            print('\t', len(tb_tree[i][j]), end='')
        print()
    
    for r, c in tree_list: # test
        print(f'({r}, {c}) =>', tb_tree[r][c])

    if year_count == K:
        break

tree_count = get_tree_count(tb_tree)

print(tree_count)