import random
difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
if difficulty == "easy":    
    number = random.randint(1, 10)
    attempts = 5
elif difficulty == "medium":
    number = random.randint(1, 50)
    attempts = 10
elif difficulty == "hard":
    number = random.randint(1, 100)
    attempts = 15
else:
    print("Invalid difficulty level. Please choose easy, medium, or hard.")
    exit()  
print(f"You have {attempts} attempts to guess the number between 1 and {number}.")
for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempt} attempts!")
        break
def get_question():
    return {
        'question': f"Guess the number between 1 and {number}",
        'attempts_left': attempts
    }
if difficulty == "easy":    
    number = random.randint(1, 10)
    attempts = 5