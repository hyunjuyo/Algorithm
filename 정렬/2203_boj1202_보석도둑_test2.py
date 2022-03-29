import sys
from collections import deque

N, K = map(int, input().split())
gold = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    gold.append((V, M))
bag = []
for _ in range(K):
    C = int(sys.stdin.readline())
    bag.append(C)

gold.sort(key=lambda x:(-x[0], x[1])) # 가격 높은 순서, 무게 가벼운 순서
bag.sort()

status = []
result = 0
q = deque(gold)
while q and K:
    price, weight = q.popleft()
    print('-'*50, 'price, weight :', price, weight) # test
    print('bag :', bag) # test

    idx = int(1e9)
    l = 0
    r = K-1
    while l <= r:
        mid = (l + r) // 2
        if bag[mid] < weight:
            l = mid + 1
        else:
            idx = min(idx, mid)
            r = mid - 1
    print('idx :', idx) # test
    
    if idx < int(1e9):
        status.append(price)
        result += price
        print(status) # test
        bag.pop(idx)
        K -= 1

print(result)