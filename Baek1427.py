
user_input = list(input())
user_result =0

for i in range(len(user_input)):
    for j in range(len(user_input)):
        if user_input[i] > user_input[j]:
            user_input[i], user_input[j] = user_input[j], user_input[i]
            user_result = user_input

user_result = [int (i) for i in user_input]

for i in range(len(user_result)):
    print(user_result[i], end = '')
