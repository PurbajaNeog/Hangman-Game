#hangman-game

import random
from words import wordlist

def get_word():
    word = random.choice(wordlist)
    return word

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'.")
            
            else:
                if guess in word:
                    print(f"Good job. '{guess}' is in the word.")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    count = 0
                    for i in word:
                        if guess == i:
                            word_as_list[count] = guess
                        count += 1
                    word_completion = "".join(word_as_list)
                        
                    if "_" not in word_completion:
                        guessed = True
                else:
                    print(f"'{guess}' is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                        

        elif len(guess) == len(word) and guess.isalpha(): 
            if guess in guessed_words:
                print(f"You already guessed '{guess}'.")
            elif guess == word:
                guessed = True
                word_completion = word
            else:
                print(f"'{guess}' is not the word.")
                guessed_words.append(guess)
                tries -= 1
        else:
            print("Not a valid input.\n")
        print(display_hangman(tries))
        print(word_completion)
    if guessed:
        print("Congratulations! You guessed the word! You win.")
    else:
        print("Sorry you ran out of tries! You lose.")
        print(f"The word was {word}.")

def display_hangman(tries):
    stages = ["""
                |_______________
                |              |
                |              
                |             
                |              
                |              
                _
                """,
                """
                |_______________
                |              |
                |              O
                |              
                |              
                |              
                _
                ""","""
                |_______________
                |              |
                |              O
                |              |
                |              |
                |              
                _
                ""","""
                |_______________
                |              |
                |              O
                |             /|
                |              |
                |              
                _
                ""","""
                |_______________
                |              |
                |              O
                |             /|\\
                |              |
                |              
                _
                """,
                """
                |_______________
                |              |
                |              O
                |             /|\\
                |              |
                |             / 
                _
                """,
                """
                |_______________
                |              |
                |              O
                |             /|\\
                |              |
                |             / \\
                _
                """]
    return stages[6-tries]

if __name__ == "__main__": 
    play(get_word())
