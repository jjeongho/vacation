
bur = [0]*3
drink = [0]*2

result1 = 0
result2 = 0

for i in range(3):
    bur[i] = int(input())


for i in range(2):
    drink[i] = int(input())

result1 = min(bur)
result2 = min(drink)

print(result1 + result2 - 50)
