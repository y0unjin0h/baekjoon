import sys
Num = int(sys.stdin.readline())

stack = []

for i in range(Num):
    option = sys.stdin.readline().split()
    if option[0] == "push":
        stack.append(option[1])
    elif option[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif option[0] == "size":
        print(len(stack))
    elif option[0] == "empty":
        print(1 if len(stack)==0 else 0)
    elif option[0] == "top":
        print(-1 if len(stack)==0 else stack[-1])


"""
이때, input() 함수를 사용할 경우, 시간초과 에러가 뜨므로 시간단축을 위해 sys.stdin.readline()을 사용한다.
입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
---------------------
Num = int(input())

stack = []
top = -1

for i in range(Num):
    option = input().split()
    if option[0] == "push":
        stack.append(option[1])
        top += 1
    elif option[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
            top -= 1

    elif option[0] == "size":
        print(len(stack))

    elif option[0] == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif option[0] == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[top])
------------------------------
Num = int(input())

stack = []
top = -1

for i in range(Num):
    option = input().split()
    if option[0] == "push":
        stack.append(option[1])
        top += 1
    elif option[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
            top -= 1
    elif option[0] == "size":
        print(len(stack))
    elif option[0] == "empty":
        print(1 if len(stack)==0 else 0)
    elif option[0] == "top":
        print(-1 if len(stack)==0 else stack[top])
------------------------------
Num = int(input())

stack = []

for i in range(Num):
    option = input().split()
    if option[0] == "push":
        stack.append(option[1])
    elif option[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif option[0] == "size":
        print(len(stack))
    elif option[0] == "empty":
        print(1 if len(stack)==0 else 0)
    elif option[0] == "top":
        print(-1 if len(stack)==0 else stack[-1])
------------------------------     
"""
