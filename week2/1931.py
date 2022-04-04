import sys
room,cnt,minEnd = [], 0, 0
N = int(sys.stdin.readline())
for i in range(N):
    ex = list(map(int,sys.stdin.readline().split()))
    room.append(ex)

room.sort(key=lambda x:(x[1],x[0])) #x[1]로 오름차순 정렬하되 같은 경우는 x[0]으로 오름차순 정렬

#가장 빨리 끝나는 회의를 고르자
for start, end in room:
    if start >= minEnd:
        minEnd = end
        cnt += 1

print(cnt)

"""
room,cnt, minEnd = [], 0, 0
N = int(input())
for i in range(N):
    ex = list(map(int,input().split()))
    room.append(ex)


#가장 빨리 끝나는 회의를 고르자
while len(room) != 0:
    room.sort(key=lambda x:x[1])
    minEnd = room[0][1]
    del room[0]
    cnt += 1
    room.sort(key=lambda x:x[0])
    i = 0
    for num in room:
        if num[0]<minEnd:
            i += 1
        else:
            break
    del room[:i]
print(cnt)
--------------------------
import sys
room,cnt,minEnd = [], 0, 0
N = int(sys.stdin.readline())
for i in range(N):
    ex = list(map(int,sys.stdin.readline().split()))
    room.append(ex)

room.sort(key=lambda x:x[0]) # 끝나는 시간이 같으면 빨리 시작하는 것부터 회의 시작  중복도 생각해줘야함!!
room.sort(key=lambda x:x[1])
#가장 빨리 끝나는 회의를 고르자

for start, end in room:
    if start >= minEnd:
        minEnd = end
        cnt += 1

print(cnt)
"""
