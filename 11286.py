import sys, heapq

heap = []
next = 0
N = int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())

    if x: #튜플로 설정함으로써 1번째로 튜플 첫 번째 원소로 나열하고 첫 번째가 중복될 시 두 번째 원소를 통해 배열함 
        heapq.heappush(heap, (abs(x),x))
    else:
        if len(heap):
            print(heapq.heappop(heap)[1]) 
        else:
            print(0)  
            
"""
import sys, heapq

heap = []
next = 0
N = int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())

    if x: 
        heapq.heappush(heap, (abs(x),x))
    else:
        if len(heap):
            for j in range(len(heap)): #애초에 튜플로 정렬이 되기 때문에 이걸 할 필요가 x
                if heap[0][0] == heap[j][0] and heap[0][1] > heap[j][1]:
                    next = j
                    break
            print(heap[next][1])
            del heap[next]
            next = 0
        else:
            print(0)  
"""
