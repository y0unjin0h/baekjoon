import sys, heapq

heap = []
N = int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())

    if x: 
        heapq.heappush(heap, x)
    else:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)      
