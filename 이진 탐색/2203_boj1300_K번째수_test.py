N = int(input())
K = int(input())

# 그룹별 시작지점 index 정보 저장
group_idx = [1] # index 1부터 시작
for i in range(1, N+1):
    group_idx.append(group_idx[i-1] + i)
for j in range(N-1, 1, -1):
    i += 1
    group_idx.append(group_idx[i-1] + j)

print(group_idx) # test

group_num = -1
group_idx2 = -1
for i, v in enumerate(group_idx):
    if v <= K:
        group_num = i + 2 # 2부터 그룹명 시작
        group_idx2 = K - v # 해당 그룹 내 index 정보 저장

print('group_num :', group_num) # test

# 해당 그룹 세부정보 초기화
group_list = []
for num in range(1, N+1):
    if group_num - num < N and num < group_num:
        group_list.append(num * (group_num - num)) # 해당 숫자 곱한 결과 리스트에 추가

group_list.sort() # 오름차순 정렬
print('group_list :', group_list) # test

print(group_list[group_idx2]) # 최종 index 반영해 결과 출력