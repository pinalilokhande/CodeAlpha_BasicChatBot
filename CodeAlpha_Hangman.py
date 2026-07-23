import random

words = ["python", "apple", "school", "computer", "mango"]

secret_word = random.choice(words)

display = []

for letter in secret_word:
    display.append("_")

lives = 6

print("================================")
print("🎮 Welcome to Hangman Game")
print("================================")

while lives > 0:

    print("\nWord:", " ".join(display))
    print("Lives Left:", lives)

    guess = input("Guess a letter: ").lower()

    if guess in secret_word:

        print("✅ Correct Guess!")

        for position in range(len(secret_word)):
            if secret_word[position] == guess:
                display[position] = guess

        # Check if player has guessed the whole word
        if "_" not in display:
            print("\n🎉 Yay! You guessed it right!")
            print("🏆 Congratulations! You Won the Game.")
            print("The word was:", secret_word)
            break

    else:

        lives -= 1
        print("❌ Wrong Guess!")

if lives == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)