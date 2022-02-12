# ------------------------------------------------------
# # 구현 아이디어
# 1. 키 차이를 구해 별도 리스트로 저장
# 2. 키 차이가 큰 지점들을 기준으로 조를 나눈 뒤, 티셔츠 제작 비용 계산  
# ------------------------------------------------------

import sys

N, K = map(int, input().split())

students = list(map(int, input().split()))

diff_list = [] # 키 차이 정보 저장
info_list = [] # (키 차이, index) 정보 저장
for i in range(N - 1):
    diff = students[i+1] - students[i]
    diff_list.append(diff)
    info_list.append((diff, i))

info_list.sort() # 키 차이 기준 오름차순 정렬

# 조 구분을 위한 index 기준점 추출
index_list = []
for _ in range(K - 1):
    diff, index = info_list.pop() # 키 차이가 큰 순서로 index 저장 
    index_list.append(index)

index_list.sort()

# 각 조에 대한 티셔츠 제작 비용 계산
cost_list = []
index_n = len(index_list)
for i in range(index_n):
    if i == 0:
        group = students[:index_list[i]+1]
    else:
        group = students[index_list[i-1]+1:index_list[i]+1]
    cost = group[-1] - group[0]
    cost_list.append(cost)

    if i == index_n - 1:
        group = students[index_list[i]+1:]
        cost = group[-1] - group[0]
        cost_list.append(cost)

if K == 1: # 조의 개수가 1개인 경우 예외처리 !!!!!
    cost_list = [students[-1] - students[0]]

# print(cost_list) # test
print(sum(cost_list))