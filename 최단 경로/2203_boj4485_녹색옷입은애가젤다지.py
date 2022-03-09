import sys

def dfs(pos, r, N):
    # print('[before]r :', r) # test
    py = pos[0]
    px = pos[1]
    r += table[py][px] # 현재 위치 도둑루피 크기 더하기
    if py == N - 1 and px == N - 1:
        # print('[after]r :', r) # test
        min_num_list.append(r) # 오른쪽 아래칸에 도달한 시점의 r값 기준 min_num 업데이트
        print(py, px, min_num_list) # test
        return

    dir = [(0, 1), (1, 0)] # 동, 남
    for i in range(2):
        ny = py + dir[i][0]
        nx = px + dir[i][1]
        if ny < N and nx < N:
            dfs((ny, nx), r, N)

i = 1
while True:
    N = int(input())
    if N == 0:
        break
    table = []
    for _ in range(N):
        table.append(list(map(int, sys.stdin.readline().split())))

    min_num_list = []
    r = 0
    dfs((0, 0), r, N)
    print('Final :', min_num_list) # test
    print(f'Problem {i}:', min(min_num_list)) # 결과 출력
    i += 1