#Using Generator and Yield as return
import random

def number_generator(limit):
    while True:
        yield random.randint(1, limit)

print("🎮 Guess the Number Game!")
print("I'm thinking of a number between 1 and 100")

gen = number_generator(100)
games_played = 0  

while True: 
    secret = next(gen)  
    attempts = 5
    games_played += 1

    print(f"\n--- Game #{games_played} ---")
    print("You have 5 attempts!\n")

    while attempts > 0:  
        guess = int(input(f"Attempts left {attempts}. Your guess: "))

        if guess == secret:
            print(f"🎉 Correct! The number was {secret}!")
            break
        elif guess < secret:
            print("📈 Too low!")
        else:
            print("📉 Too high!")

        attempts -= 1

        if attempts == 0:
            print(f"💀 Game over! The number was {secret}")

    again = input("\nPlay again? (yes/no): ")
    if again.lower() != "yes":
        print(f"\nThanks for playing! You played {games_played} game(s). Goodbye! 👋")
        break  
