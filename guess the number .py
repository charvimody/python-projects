import random
def playgame():
 print ("\nWelcome to the Guess the Number Game! 🎮 ")
print ("INSTRUCTIONS: I'm thinking of a number between 1 and 100 . You have 5 attempts to guess the number.")
print ("After each guess, I will tell you if your guess is too high, too low, or correct.")
print ("there will be difficulty levels to choose from the number 1 2 and 3 choose the number according to ur difficulty level ")
print ("Good luck!")
print("Choose a difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")
choice = input("Enter choice: ")  
if choice == "1":
        limit = 20
        attempts = 5

elif choice == "2":
        limit = 50
        attempts = 7

else:
        limit = 100
        attempts = 10

secret = random.randint(1, limit)
score = attempts * 10

while attempts > 0:

        guess = int(input(f"\nGuess number (1-{limit}): "))

        if guess == secret:
            print("🎉 Correct!")
            print("Score:", score)
            break

        elif guess < secret:
            print("⬆ Too Low")
        else:
            print("⬇ Too High")
        
        attempts -= 1
        score -= 10

        print("Attempts left:", attempts)

        if attempts == 0:
         print("\nGame Over")
         print("Correct Number was:", secret)

again = input("\nPlay Again? (yes/no): ").lower()
if again == "yes":
        playgame()
elif again == "no":
        print("\nThanks for playing! 👋")

else:
     print("\nInvalid input. Please enter yes or no.")
playgame()