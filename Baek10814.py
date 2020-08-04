N = int(input())

word = []

for _ in range(N):
    [x, y] = map(str,input().split())
    word.append([x,y])

word.sort()

for i in range(N):
     print(*(word[i]))