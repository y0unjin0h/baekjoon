import sys

N, K = map(int,sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for i in range(N)]
A.reverse() # 내림차순으로 변경

count = 0

for Coin in A:
    if K//Coin > 0: # 몫이 있으면 계산하면서 깎아감
        CoinNum, K = divmod(K, Coin) # 몫, 나머지 K를 줄여감
        count += CoinNum
print(count)

"""
import sys

N, K = map(int,input().split())
A = []
count, sum = 0, 0
maxCoin = 0

for i in range(N):
    A.append(int(input()))

A = sorted(A, reverse = True)

while sum != K:
    for maxCoin in A:
        if maxCoin + sum <= K:
            sum += maxCoin
            count += 1
            if sum == K:
                print(count)
            break
-----------import sys

N, K = map(int,sys.stdin.readline().split()))
A = []
count, sum = 0, 0
maxCoin = 0

for i in range(N):
    A.append(int(sys.stdin.readline()))

A .reverse()

while sum != K:
    for maxCoin in A:
        if maxCoint + sum > K:
            del A[0] #이렇개 하면 2칸 씩 건너뛰어 포문 출력됨 이상하게 출력되니 조심
        elif maxCoin + sum <= K:
            sum += maxCoin
            count += 1
            if sum == K:
                print(count)
            break
-------------------------
import sys

N, K = map(int,sys.stdin.readline().split())
A = []
count, sum = 0, 0
maxCoin = 0

for i in range(N):
    A.append(int(sys.stdin.readline()))

A = sorted(A, reverse = True)

while sum != K:
    for maxCoin in A:
        if maxCoin + sum <= K:
            sum += maxCoin
            count += 1
            del A[:A.index(maxCoin)]
            if sum == K:
                print(count)
            break
------------------------------------
"""
