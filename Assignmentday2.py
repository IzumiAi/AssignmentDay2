import random

def lotto_game():
    winning_numbers = [random.randint(1, 100) for _ in range(3)]
    print("Welcome to the Lotto Game!")
    print("Please choose 3 numbers between 1 and 100:")

    user_numbers = []
    for i in range(3):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                if 1 <= num <= 100:
                    user_numbers.append(num)
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    if sorted(user_numbers) == sorted(winning_numbers):
        print(" Congratulations! You won the jackpot!")
    else:
        matches = sum(1 for num in user_numbers if num in winning_numbers)
        if matches == 2:
            print("You partially won! Two of your numbers match the winning numbers.")
        elif matches == 1:
            print("You partially won! One of your numbers matches the winning numbers.")
        else:
            print("Sorry, you didn't win this time. Better luck next time!")

    print(f"The winning numbers were: {winning_numbers}")

lotto_game()