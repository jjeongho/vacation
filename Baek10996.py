N = int(input())

for i in range(N):
    for i in range(1, N+1):
        if(i%2 == 1):
            print("*", end='')
        else:
            print(" ", end='')

    print()
    for i in range(0, N):
        if(i%2 == 0):
            print(" ", end='')
        else:
            print("*", end='')
    print()