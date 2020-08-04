N = int(input())

word = []

for _ in range(N):
    word.append(str(input()))

word =list(set(word))

word.sort(key = lambda x:(len(x),x))

print(*word, sep='\n')

