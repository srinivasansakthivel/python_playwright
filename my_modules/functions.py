def greetings(name):
    print("Helllo, World,", name)



def user_guessing_game(secret_number, stop_chars):
    user_input = ""
    while user_input != stop_chars:
        user_input = input("\n\nEnter a number: ")
        if user_input == secret_number:
            print("Bingo!")
        else:
            print(f"The number is {user_input}, Try again....")


