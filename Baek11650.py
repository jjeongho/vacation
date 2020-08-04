N = int(input())
num = []

for _ in range(N):
    [x, y] = map(int,input().split())
    num.append([x,y])



for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]


for i in range(N):
    print(*(num[i]))

