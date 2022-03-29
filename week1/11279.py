import sys, heapq

heap = []
N = int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())

    if x:  # 최소 힙을 지원하기 때문에 -를 붙여 최대 힙으로 수정
        heapq.heappush(heap, -x)
    else:
        if len(heap):
            print(-heapq.heappop(heap))
        else:
            print(0)      
