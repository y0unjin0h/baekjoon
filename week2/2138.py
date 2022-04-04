import copy

N = int(input())
A1 = list(map(int,list(input())))
B = list(map(int,list(input())))
TF1,TF2, change_cnt, non_cnt = False, False, 0, 0
A2 = copy.deepcopy(A1)

def change(x):
    num = 0 if x else 1
    return num

if A1 == B:
    print(0)
    exit(0)

for i in range(N):
    if i == 0:
        A1[i] = change(A1[i])
        A1[i+1] = change(A1[i+1])
        change_cnt += 1
    else:          
        if A1[i-1] != B[i-1]:
            if i == N-1:
                A1[i-1] = change(A1[i-1])
                A1[i] = change(A1[i])
            else:
                A1[i-1] = change(A1[i-1])
                A1[i] = change(A1[i])
                A1[i+1] = change(A1[i+1])
            change_cnt += 1
    if A1 == B:
        TF1 = True
        break

for i in range(N):
    if i == 0:
        pass
    else:          
        if A2[i-1] != B[i-1]:
            if i == N-1:
                A2[i-1] = change(A2[i-1])
                A2[i] = change(A2[i])
            else:
                A2[i-1] = change(A2[i-1])
                A2[i] = change(A2[i])
                A2[i+1] = change(A2[i+1])
            non_cnt += 1
    if A2 == B:
        TF2 = True
        break  

if TF1 and TF2:
    print(min(change_cnt,non_cnt))
elif TF1:
    print(change_cnt)
elif TF2:
    print(non_cnt)
else:
    print(-1)
"""
N = int(input())
A = list(map(int,list(input())))
B = list(map(int,list(input())))
TF, cnt = True, 0

def change(x):
    num = 0 if x else 1
    return num

for i in range(N):
    if A[i] != B[i]:
        if i == 0:
            change(A[i])
            change(A[i+1])
        elif i == N-1:
            change(A[i-1])
            change(A[i])
        else:
            change(A[i-1])
            change(A[i])
            change(A[i+1])
        cnt += 1         

for i in range(N):
    if A[i] != B[i]:
        TF = False

if TF:
    print(cnt)
else:
    print(-1)   
"""
