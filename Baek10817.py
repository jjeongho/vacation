import sys


def bubblesort()
num = list(map(int, sys.stdin.readline().split()))
sum = 0

for i in range(3):
    for j in range(2):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
            sum = num


