# setup
import random
words=["lizard", "games", "rings", "brand", "insect", "phone"]
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
secret_word=random.choice(words)
guessed_letters=[]
incorrect_guesses = 0
max_guesses = 6
is_running=True
active=True
wins=0
loses=0

# function 1 display word
def display_word():
 global hint
 global max_guesses
 global incorrect_guesses
 global is_running
 hint=[" _ "]*len(secret_word)
 while is_running:
    guess=input("Please guess a letter: ").lower()
    if guess in alphabet:
        alphabet.remove(guess)
    else:
        print("You've already guessed that letter")
        display_word()
    guessed_letters.append(guess)
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i]==guess:
                hint[i]=guess
                print(" ".join(hint))
    else:
        print("WRONG LOL")
        incorrect_guesses=incorrect_guesses+1
        max_guesses=max_guesses-1
    check_game_status()
    print(f"used letters: "+", ".join(guessed_letters))
    print(f"remaining guesses: {max_guesses}")
    print(f"incorrect guesses: {incorrect_guesses}\n")

# function 2 check game status
def check_game_status():
        global hint_str
        global is_running
        global wins
        global loses
        global alphabet
        global guessed_letters
        global incorrect_guesses
        global max_guesses
        hint_str = "".join(hint)
        if hint_str in secret_word:
            print("Congrats - you win\n")
            wins=wins+1
            is_running=False
            alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z"]
            guessed_letters = []
            incorrect_guesses = 0
            max_guesses = 6
            play_game()
        if max_guesses<=0:
            print(f"You lose!\nThe word was: {secret_word}\n")
            loses=loses+1
            is_running=False
            alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z"]
            guessed_letters = []
            incorrect_guesses = 0
            max_guesses = 6
            play_game()

def play_game():
    global active
    global is_running
    global wins
    global loses
    while active:
        print("Welcome to Kelsey's Hangman!")
        print("1. Play Hangman")
        print("2. Display Stats")
        print("3. Quit")
        menu_choice=input("Select an option: ")
        if menu_choice=="1":
            is_running=True
            display_word()
        if menu_choice=="2":
            print(f"Games won: {wins}")
            print(f"Games lost: {loses}\n")
            play_game()
        if menu_choice=="3":
            active=False
        else:
            print("Invalid option\n")

# call main function
play_game()