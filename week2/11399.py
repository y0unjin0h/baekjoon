N = int(input())
P = list(map(int,input().split()))
time, total = 0, 0

P.sort()

for i in P:
    time += i
    total += time
print(total)
