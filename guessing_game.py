import random

MINIMUM = 1
MAXIMUM = 100

def secret_number():
    return random.randint(MINIMUM,MAXIMUM)

def check_response(secret, guess):
    if secret == guess:
        return "Correct"
    if secret < guess:
        return "Too High"
    if secret > guess:
        return "Too Low"

def get_user_input(secret):
    user_guess = int(input("Enter your guess: "))
    response = check_response(secret, user_guess)
    print(response)
    return response

def main():
    secret = secret_number()
    print(secret)
    if get_user_input(secret) == "Correct":
        return "You win"
    if get_user_input(secret) == "Correct":
        return "You win"
    if get_user_input(secret) == "Correct":
        return "You win"
    if get_user_input(secret) == "Correct":
        return "You win"
    if get_user_input(secret) == "Correct":
        return "You win"
    if get_user_input(secret) == "Correct":
        return "You win"
    
    return "Out of guesses"
    
    





if __name__ == "__main__":
    print(main())