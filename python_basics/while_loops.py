a = 0

while a < 5:
    print(f'Hello, {a}')
    a += 1


user_input = ''

while user_input != "-1":
    user_input = input("Guess a number from 1 to 100: ")
    if user_input == "77":
        print("Bingo!, you guessed the number")
    print(f'The number is {user_input}, Try again')