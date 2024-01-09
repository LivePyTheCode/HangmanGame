import random
from wordlisthangman import word_list
from arthangman import hangman_logo, hangman_logo_2, hangman_logo_3, hangman_logo_4, hangman_stages

chosen_word = random.choice(word_list)
print(hangman_logo_4)
print(hangman_logo)
print("Welcome to Animal Hangman!")

lives = 7
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}!")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print(f"The word is {chosen_word}!")
        print("You win the Game!😁")
        print(hangman_logo_3)
    if guess not in chosen_word and lives:
        lives -= 1
        print(hangman_stages[lives-7])
        print("This letter is not in the word! You have lost a life!")
    if lives == 0:
        end_of_game = True
        print(f"{chosen_word} was the word!")
        print("You Lose!😭")
        print(hangman_logo_2)

