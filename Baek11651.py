import sys


N=int(sys.stdin.readline())

num=[]

for _ in range(N):
    num.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    num[i][0],num[i][1]=num[i][1],num[i][0]

for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j],   num[i]


for i in range(N):
    num[i][0],num[i][1]=num[i][1],num[i][0]
    print(num[i][0], num[i][1])
