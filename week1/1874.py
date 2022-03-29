import sys
N = int(sys.stdin.readline())
stack, output, error, num = [], [], False, 1

for i in range(N):
    cur = int(sys.stdin.readline())

    #stack에 cur이 없어 필요한 stack 값을 push하는 단계
    while cur >= num: # cur이 스택에 없으면 stack에 계속 추가 (num의 값을 계속 증가시키며 추가)  
        stack.append(num) 
        output.append("+")
        num += 1

    #stack에 cur이 있는 상태
    if stack[-1] == cur:#stack의 top과 cur이 같으면 pop
        stack.pop()
        output.append("-")
    else: #stack의 값이 
        error = True

if error:
    print("NO")
else:
    print(*output, sep= "\n")
    
"""
import sys
N = int(input())
num = list(range(1,N+1))
stack = []
output = []
error = 0 

for i in range(N):
    cur = int(input())

    if cur in stack:
        if stack[-1] != cur:
            error = 1
        else:
            del stack[-1]
            output.append("-")
        
    else:
        while cur in num:
            stack.append(num.pop(0))
            output.append("+")
        if stack[-1] == cur:
            del stack[-1]
            output.append("-")

if error == 0:
    for i in output:
        print(i)
else:
     print("NO")
--------------------------
import sys
N = int(sys.stdin.readline())
num = list(range(1,N+1))
stack = []
output = []
error = 0 

for i in range(N):
    cur = int(sys.stdin.readline())

    if cur in stack:
        if stack[-1] != cur:
            error = 1
        else:
            del stack[-1]
            output.append("-")
        
    else:
        while cur in num:
            stack.append(num.pop(0))
            output.append("+")
        del stack[-1]
        output.append("-")

if error == 0:
    for i in output:
        print(i)
else:
     print("NO")
--------------------------
import sys
N = int(sys.stdin.readline())
num = list(range(1,N+1))
stack, output, error = [], [], False

for i in range(N):
    cur = int(sys.stdin.readline())

    if cur not in stack:
        while cur in num:
            stack.append(num.pop(0))
            output.append("+")
    if stack[-1] == cur:
        stack.pop()
        output.append("-")
    else:
        error = True

if error:
    print("NO")
else:
    print(*output, sep="\n")
"""
