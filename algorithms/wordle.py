import random

hidden = ['Hello', 'Sorry', 'Earth', 'Brush']

word = random.choice(hidden).lower()

tries = 0

while tries < 6:
    
    guess = input("Enter your guess:").lower()
    colored_guess = " "

    for g,w in zip(guess,word) :

        if g == w:
            colored_guess += f"\033[32m{g}\033[0m"

        elif g in word:
            colored_guess += f"\033[33m{g}\033[0m"
        
        else:
            colored_guess += g

    print(colored_guess)

    if guess == word:
        print("Congrats! You guessed the word!")
        break

    tries += 1

if tries == 6 and guess != word:
    print(f"Out of tries! The word was {word}")

