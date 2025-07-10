from random import randint
def main_loop():
    print("---NUMBER GUESSING GAME---")
    while True:
        number = randint(20,30)
        guess = 3
        while guess > 0:
            try:
                user_guess = int(input("Pick a number between 20-30: "))
                if user_guess < 20 or user_guess > 30:
                    raise ValueError("Invalid Input")
                if user_guess == number:
                    print(f"Number was {number}, congratulations you guessed it right!")
                    while True:
                        again = input("Do you wanna play again? (yes/no): ").lower()
                        if again == "yes":
                            return main_loop()
                        elif again == "no":
                            exit()
                        else:
                            print("Invalid input. Please only type yes or no")
                elif user_guess > number:
                    guess -= 1
                    print(f"You need to lower the number, you have {guess} guesses left")
                else:
                    guess -= 1
                    print(f"You need to increase the number, {guess} guesses left")
            except ValueError:
                print("Invalid input, enter a number between 20-30")
        if guess == 0:
            print("Game over, number was: ", number)
            while True:
                again = input("Do you wanna play again? (yes/no): ").lower()
                if again == "yes":
                    break
                elif again == "no":
                    exit()
                else:
                    print("Invalid input. Please only type yes or no")
main_loop()