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

print(gold) # test
print(bag) # test

status = [0] * K
k_count = K
result = 0
q = deque(gold)
while q and k_count:
    price, weight = q.popleft()
    print('price, weight :', price, weight) # test
    for i in range(K):
        if bag[i] >= weight and status[i] == 0:
            print('bag', i) # test
            status[i] = price
            result += price
            print(status) # test
            k_count -= 1
            break

print(result)