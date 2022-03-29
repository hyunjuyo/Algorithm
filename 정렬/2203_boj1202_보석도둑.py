import sys
import heapq
from collections import deque

N, K = map(int, input().split())
gold = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    gold.append((M, V))
bags = []
for _ in range(K):
    C = int(sys.stdin.readline())
    bags.append(C)

gold.sort()
bags.sort()

result = 0
q = deque(gold)
h = []
for bag in bags:
    # print('bag :', bag) # test
    while q and q[0][0] <= bag:
        price, weight = q.popleft()
        heapq.heappush(h, -weight)
        # print('heapq :', h) # test
    if h:
        result += heapq.heappop(h)
        # print('result :', result) # test

print(-result)