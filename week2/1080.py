N, M = map(int, input().split())
TF, cnt = True, 0
A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]

def convert(x,y): # 3X3 행렬 변환 
    for i in range(x,x+3):
        for j in range(y,y+3):
            A[i][j]  = 0 if A[i][j] else 1

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]: # 행렬이 다를 시
            convert(i,j) #한번 변환한 것은 건드리지 x
            cnt += 1

for i in range(N): #A,B 맞는지 체크
    for j in range(M):
        if A[i][j] != B[i][j]:
            TF = False

if TF:
    print(cnt)
else:
    print(-1)       
"""
import sys #왜 런타임 에러 뜨는거지?

N, M = map(int,sys.stdin.readline().split())
TF, cnt = True, 0
A = [list(map(int,list(sys.stdin.readline()))) for _ in range(N)]
B = [list(map(int,list(sys.stdin.readline()))) for _ in range(N)]


def convert(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            A[i][j]  = 0 if A[i][j] else 1

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            convert(i,j)
            cnt += 1

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            TF = False
            break

if TF:
    print(cnt)
else:
    print(-1)       
"""
