#I added a scoring system so if the user guessess less then 10 times they get a score out of 10 but if they guess more then 10 times their score goes to 0/10
import random

def generate_hint(secret_word, guess):
    hint = []
    
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:  # If correct letter is in the right spot
            hint.append(guess[i].upper())
        elif guess[i] in secret_word:  # If letter is correct but not in the right spot
            hint.append(guess[i].lower())
        else:  # Letter not correct is _
            hint.append("_")
    
    return " ".join(hint)

def word_guessing_game():
    secret_word = "testing"
    attempts = 0
    
    print("Welcome to the word guessing game!")
    print("For legal reasons, this is not associated with Wordle.")
    print("Your hint is:", "_ " * len(secret_word))
    
    while True:
        guess = input("What is your guess? ").strip().lower()
        attempts += 1
        
        if len(guess) != len(secret_word):
            print("Your guess must match the number of letters in the secret word.")
            continue
        
        if guess == secret_word: # displays at the ennd of the game and shows if they guessed less then 10 they get a score out of 10 on how well they guessed
            print("You did it! Nice job.")
            print(f"It took you {attempts} guesses.")
            
            if attempts <= 2:
                score = 10
            elif attempts <= 4:
                score = 8
            elif attempts <= 6:
                score = 6
            elif attempts <= 8:
                score = 4
            elif attempts <= 10:
                score = 2
            else:
                score = 0
            
            print(f"You guessed the word in {attempts} attempts. You get a score of ({score}/10).")
            break
        
        hint = generate_hint(secret_word, guess)
        print("Your hint is:", hint)

# Runs the game on start
word_guessing_game()