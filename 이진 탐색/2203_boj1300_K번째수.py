def get_count(mid):
    res = 0
    for num in range(1, N+1):
        res += min(N, mid // num) # 1부터 N까지 가능한 케이스 개수 더하기
    
    return res

N = int(input())
K = int(input())

result = 100000**2 + 1
l = 1
r = 100000**2
while l <= r:
    mid = (l + r) // 2
    count = get_count(mid)
    print('-'*20, 'count :', count) # test

    if count >= K:
        result = min(result, mid)
        r = mid - 1
    else:
        l = mid + 1

    print('mid :', mid) # test
    print('result :', result) # test

print(result)