import sys
sys.setrecursionlimit(100000)

# 최상위 그룹명 찾기 함수
def find(x):
    if x == group[x]:
        return x
    else:
        group[x] = find(group[x])
        return group[x]

def union(a, b):
    group_a = find(a)
    group_b = find(b)

    if group_a == group_b:
        return
    else:
        group[group_b] = group_a # 상위 그룹 정보 입력
        count[group_a] += count[group_b] # 개수 합치기

CASE = int(input())
result = []
for _ in range(CASE):
    F = int(input())
    group = {}
    count = {}
    for _ in range(F):
        A, B = sys.stdin.readline().split()
        if group.get(A) == None: # 기존에 없는 경우
            group[A] = A
            count[A] = 1
        if group.get(B) == None: # 기존에 없는 경우
            group[B] = B
            count[B] = 1

        union(A, B)
        # print(group) # test
        # print(count) # test
        # print(A)
        result.append(count[find(A)])

print(*result, sep='\n')