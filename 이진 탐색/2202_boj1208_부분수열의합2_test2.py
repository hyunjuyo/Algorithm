N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for bit in range(1, 1<<N): # 1부터 시작
    print('-'*20, 'bit : ', bin(bit), '-'*20) # test
    sub_arr = []
    for i in range(N):
        # print(bit & (1<<i), arr[i]) # test
        if bit & (1<<i) > 0:
            sub_arr.append(arr[i])
    print(sub_arr) # test
    if sum(sub_arr) == S:
        print("********** here~!! **********") # test
        count += 1

print(count)