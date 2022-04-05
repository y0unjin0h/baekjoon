import sys, heapq

room, queue = [], []
N = int(input())

for i in range(N):
    ex = list(map(int,input().split()))
    room.append(ex)

room.sort(key=lambda x:x[0])
heapq.heappush(queue, room[0][1])

for i in range(1,N):
    if room[i][0] < queue[0]:
        heapq.heappush(queue,room[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue,room[i][1])


print(len(queue))
