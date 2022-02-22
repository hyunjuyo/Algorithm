import sys
sys.setrecursionlimit(100000)

def dfs(a):
    global count

    info[a][0] = line_num+1 # 방문 표시
    for i, b in enumerate(info[a]):
        if i > 0 and info[b][0] < line_num+0: # 이전에 방문하지 않았던 경우
            info[b][0] = line_num+0 # 초기화
        if i > 0 and info[b][0] == line_num+0: # 아직 방문하지 않은 경우
            count += 1
            dfs(b)

CASE = int(input())
result = []
line_num = 0
for _ in range(CASE):
    F = int(input())
    info = {}
    for _ in range(F):
        line_num += 1
        A, B = sys.stdin.readline().split()
        if info.get(A) == None:
            info[A] = [line_num+0] # 첫번째 정보에 방문여부
        info[A].append(B)
        if info.get(B) == None:
            info[B] = [line_num+0]
        info[B].append(A)

        count = 1
        # for v in info.keys(): # 방문여부 초기화
        #     info[v][0] = False
        # print(info) # test
        dfs(A)
        # print(A, info) # test
        result.append(count)

for v in result:
    print(v)