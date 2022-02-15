
def get_sub_sum_list(arr_name):
    lth = len(arr_name)
    sub_sum_list = []
    for bit in range(1<<lth): # 0부터 시작
        sub_arr = []
        for i in range(lth):
            if bit & (1<<i):
                sub_arr.append(arr_name[i])
        sub_sum_list.append(sum(sub_arr))
    
    return sub_sum_list, len(sub_sum_list)

def get_num_count(num, idx, lth, sub_sum_list):
    num_count = 1
    while True:
        idx += 1
        if idx == lth: # 인덱스 범위 벗어난 경우
            break
        if sub_sum_list[idx] == num:
            num_count += 1
        else:
            break
    
    return num_count, idx

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# arr 두 개로 나누기
arr_l = arr[:N//2]
arr_r = arr[N//2:]

# 두 arr별로 각 부분수열의 합 list 추출(길이도 함께 저장)
sub_sum_l, lth_l = get_sub_sum_list(arr_l)
sub_sum_r, lth_r = get_sub_sum_list(arr_r)

sub_sum_l.sort() # 오름차순 정렬
sub_sum_r.sort(reverse=True) # 내림차순 정렬

print(arr_l, sub_sum_l) # test
print(arr_r, sub_sum_r) # test

# count = 0
# for l_idx in range(len(sub_sum_l)):
#     for r_idx in range(len(sub_sum_r)):
#         if sub_sum_l[l_idx] + sub_sum_r[r_idx] == S:
#             count += 1

count = 0
idx_l = 0 
idx_r = 0
while idx_l < lth_l and idx_r < lth_r:
    num_l = sub_sum_l[idx_l]
    num_r = sub_sum_r[idx_r]
    if num_l + num_r > S:
        idx_r += 1 # 합계가 작아지는 방향
    elif num_l + num_r < S:
        idx_l += 1 # 합계가 커지는 방향
    else:
        print(idx_l, idx_r) # test
        num_l_count, idx_l = get_num_count(num_l, idx_l, lth_l, sub_sum_l)
        num_r_count, idx_r = get_num_count(num_r, idx_r, lth_r, sub_sum_r)
        count += num_l_count * num_r_count # 중복 케이스를 반영해 개수 더하기

if S == 0:
    count -= 1 # 두 arr 모두 아무것도 뽑지 않은 케이스 1개 제외

print(count)

# 6 0
# -7 -3 -2 2 3 5