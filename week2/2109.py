import sys, heapq

Class, queue = [], []
N = int(input())

for i in range(N):
    ex = list(map(int,input().split()))
    Class.append(ex)

Class.sort(key=lambda x:x[1])

for p, d in Class:
    heapq.heappush(queue, p)
    if d < len(queue):
        heapq.heappop(queue)

print(sum(queue))
