from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for lth in range(1, N+1):
    print('-'*30) # test
    print(lth) # test
    for comb in combinations(arr, lth):
        print(comb) # test
        if sum(comb) == S:
            print("********** here~!! **********") # test
            count += 1

print(count)