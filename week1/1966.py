testSize = int(input())
for i in range(testSize):
    queue = []
    num, which = map(int,input().split()) #샘플 첫 줄
    queue = list(map(int,input().split())) #샘플 두 번째 줄
	
    count = 0  
    while 1:
        if queue[0] == max(queue): #최댓값이라 나갈 경우
           count += 1
           if which == 0: #그게 which일 경우
                print(count)
                break
           else: #다른 애일 경우
                del queue[0]
                which -= 1
        else: #최대가 아니라 뒤로 빠질 경우
            queue.append(queue.pop(0))
            if which == 0: #which일 경우
                which = len(queue)-1
            else: #다른 애일 경우
                which -= 
                
                """ 푼 과정
                testSize = int(input())
for i in range(testSize):
    queue = []
    num, which = input().split()
    queue = list(map(int,input().split()))
	
    count = 0
    which = int(which) 
    while 1:
        if (queue[0] == max(queue) and which ==  0): #위치가 이제 나갈떄 일때
            del queue[0]
            count += 1
            print(count)
            break
        elif (queue[0] != max(queue) and which ==  0): #위치가 나갈때가 아닐때
            queue.append(queue[0])
            del queue[0]
            which = len(queue)-1
        elif (queue[0] == max(queue) and which !=  0): #다른애가 나갈때 일때
            del queue[0]
            count += 1
            which -= 1
        else: #다른애가 나갈떄 아닐때
            queue.append(queue[0])
            del queue[0]
            which -= 1
                """
