N = int(input())

num = []

for _ in range(N):
    num.append(int(input()))

num = sorted(num)

for i in range(N):
    print(num[i])

