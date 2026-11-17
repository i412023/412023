#1a2b game
import random

PASSWORD_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def generate_number() -> str:
    password = random.sample(PASSWORD_LIST, 4)
    string_password = "".join(map(str, password))
    return string_password

def user_input() -> str:
    while True:
        user_input = input("Enter a 4-digit number: ")
        if len(user_input) != 4 or not user_input.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
        else:
            return user_input

def check_guess(password: str, guess: str) -> tuple:
    a = 0
    b = 0
    for i in range(4):
        if(password[i] == guess[i]):
            a = a + 1
        elif(guess[i] in password):
            b = b + 1
    return a, b

if __name__ == "__main__":
    try:
        PASSWORD = generate_number()
        print("Generated password:", PASSWORD)
        while True:
            guess = user_input()
            a, b = check_guess(PASSWORD, guess)
            print(f"Result: {a}A{b}B")
            if a == 4:
                print("Success!")
                break
            else:
                pass
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")