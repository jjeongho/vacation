import sys

num = []
avg = 0
for i in range(5):
    num.append(int(sys.stdin.readline().strip()))
    if num[i] < 40:
        num[i] = 40
    avg += num[i]

print(int(avg/5))