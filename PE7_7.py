
numbers_list = []
while True:
    user_input = input("Enter a number or enter 0 to stop: ")
    if int(user_input) == 0:
        print(numbers_list)
        print(sum(numbers_list))
        print(numbers_list.mean())
        break
    else:
        numbers_list.append(int(user_input))