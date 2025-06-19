# Tic Tac Toe

''' def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    # Check for tie
    if " " not in board:
        return "Tie"
    # No winner yet
    return None

def get_move(player, board):
    while True:
        move = input("Player " + player + ", enter a move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == " ":
            return int(move) - 1
        else:
            print("Invalid move. Try again.")

def play_game():
    board = [" "]*9
    players = ["X", "O"]
    turn = 0
    while True:
        print_board(board)
        move = get_move(players[turn], board)
        board[move] = players[turn]
        winner = check_win(board)
        if winner:
            print_board(board)
            if winner == "Tie":
                print("It's a tie!")
            else:
                print("Player " + winner + " wins!")
            return
        turn = (turn + 1) % 2
        
play_game()





# Quiz Game

print("\n------------------------------------------------ QUIZ GAME ------------------------------------------------")
a=input("\n\nEnter the category you want to play for [ Sports, Geography, Science ] : ")

score = 0

if a.lower() == "geography":
    # Geography
    # Question 1
    print("\n\nQ-1 What is the capital of India?")
    answer = input("ANS: ")
    if answer.lower() == "delhi":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 2
    print("Q-2 Which is the largest planet in our Solar System?")
    answer = input("ANS: ")
    if answer.lower() == "jupiter":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 3
    print("Q-3 Which is the smallest country in the world?")
    answer = input("ANS: ")
    if answer.lower() == "vatican city":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 4
    print("Q-4 Where the Amazon Forest is located?")
    answer = input("ANS: ")
    if answer.lower() == "south america":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect. 👎🏻\n\n")

    # Question 5
    print("Q-5 Which is the nearest planet to the sun?")
    answer = input("ANS: ")
    if answer.lower() == "mercury":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    print("Your final score is " + str(score) + " out of 5.")
    print("\n------------------------------------------------ GAME OVER ------------------------------------------------")


elif a.lower() == "sports":
    # Sports
    # Question 1
    print("\n\nQ-1 Which is the national sport of India?")
    answer = input("ANS: ")
    if answer.lower() == "hockey":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 2
    print("Q-2 Which cricketer scored 100 centuries in international cricket?")
    answer = input("ANS: ")
    if answer.lower() == "sachin tendulkar":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 3
    print("Q-3 National Sports Day of India is celebrated on whose birthday anniversary?")
    answer = input("ANS: ")
    if answer.lower() == "dhyan chand":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 4
    print("Q-4 In what sport would you use a shuttlecock?")
    answer = input("ANS: ")
    if answer.lower() == "badminton":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 5
    print("Q-5 What is the name of the international men's tennis team competition?")
    answer = input("ANS: ")
    if answer.lower() == "davis cup":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    print("Your final score is " + str(score) + " out of 5.")
    print("\n------------------------------------------------ GAME OVER ------------------------------------------------")


elif a.lower() == "science":
    # Science
    # Question 1
    print("\n\nQ-1 What is the powerhouse of a cell?")
    answer = input("ANS: ")
    if answer.lower() == "mitochondria":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 2
    print("Q-2 What is the smallest unit of matter?")
    answer = input("ANS: ")
    if answer.lower() == "atom":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 3
    print("Q-3 What is the name of the force that pulls objects towards each other?")
    answer = input("ANS: ")
    if answer.lower() == "gravity":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 4
    print("Q-4 What is the process by which plants make their own food?")
    answer = input("ANS: ")
    if answer.lower() == "photosynthesis":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")

    # Question 5
    print("Q-5 What is the name of the process by which a liquid turns into a gas?")
    answer = input("ANS: ")
    if answer.lower() == "evaporation":
        print("Correct! 👍🏻\n\n")
        score += 1
    else:
        print("Incorrect! 👎🏻\n\n")
        
    print("Your final score is " + str(score) + " out of 5.")
    print("\n------------------------------------------------ GAME OVER ------------------------------------------------")


else:
    print("Please enter a valid category from the given!")







# Hangman
import random

def play_game():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    word = random.choice(words)
    guesses = []
    turns = 7
    while turns > 0:
        print("You have", turns, "guesses left.")
        progress = ""
        for letter in word:
            if letter in guesses:
                progress += letter
            else:
                progress += "-"
        print(progress)
        guess = input("Guess a letter: ")
        if guess in guesses:
            print("You already guessed that letter.")
        elif guess in word:
            print("Correct!")
            guesses.append(guess)
        else:
            print("Wrong!")
            turns -= 1
        if "-" not in progress:
            print("Congratulations! You guessed the word:", word)
            return
    print("Sorry, you ran out of guesses. The word was:", word)

play_game() '''






# Stone Paper Scissors
''' import random

def play_game():
    print("Let's play Stone-Paper-Scissors!")
    options = ["stone", "paper", "scissors"]
    while True:
        player_choice = input("Choose your weapon (stone, paper, or scissors): ")
        if player_choice not in options:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(options)
        print("You chose", player_choice)
        print("The computer chose", computer_choice)
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "stone" and computer_choice == "scissors":
            print("You win!")
        elif player_choice == "paper" and computer_choice == "stone":
            print("You win!")
        elif player_choice == "scissors" and computer_choice == "paper":
            print("You win!")
        else:
            print("You lose!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

play_game() '''








import random 
# Hangman
def hangman(): 
    print("\n------------------------------------------------ THE HANGMAN ------------------------------------------------")
    print("Save the Man by guessing The word Right Before He Gets HANGED !!!! ")
    words =("apple","banana","orange","grape","mango","watermelon","cherry") 
    dict = {'apple':"It is red in colour and eating it keeps the doctor away Guess me!",'banana':"It has yellow skin and you have to peel off to eat it Guess me!",'orange':"It is orange in colour also it is juicy and pulpy Guess me!",'cherry':"Cake is incomplete without this on the top of it Guess me!",'grape':"It is small and round also comes in bunches Guess me!",'mango':"It is called the King of Fruits. Guess me!",'watermelon':"This is large and green on the outside, with a juicy pink or red flesh inside. Guess me!"}
    word = random.choice(words)   
    print("HINT : ",dict[word]) 
    guesses = []
    turns = 7
    while turns > 0:
        print("You have", turns, "guesses left.")
        progress = ""  
        for letter in word:
            if letter in guesses:
                progress += letter
            else:
                progress += "-"
        print(progress)
        if "-" not in progress:
            print("Congratulations! You guessed the word and SAVED THE MAN !!") 
            break
        while True:
              guess = input("Guess a letter: ")
              if len(guess) == 1:
               break
              print("Please enter only a single letter.")
        if guess in guesses:
            print("You already guessed that letter.")
        elif guess in word:
            print("Correct!")
            guesses.append(guess) 
        else:
            print("Wrong!")
            turns -= 1
    if turns == 0 : 
        print("Sorry, you ran out of guesses the man is HANGED !!!! The word was: ", word)
    else:print("\n------------------------------------------------ GAME OVER ------------------------------------------------")     

# Stone Paper Knife  
def SPK(): 
    print("\n------------------------------------------------ STONE PAPER KNIFE ------------------------------------------------")
    def gameWin(comp, you):
        if comp == you:
            return None

        elif comp == 'S':
            if you=='K':
                return False
            elif you=='P':
                return True
    
        elif comp == 'P':
            if you=='S':
                return False
            elif you=='K':
                return True
    
        elif comp == 'K':
            if you=='P':
                return False
            elif you=='S':
                return True  
    quit ='Y'        
    while quit == 'Y':
        print("Let's play Stone-Paper-Knife!")
        you = input("Your Turn: Stone(S) Paper(P) or Knife(K)? : ") 
        randNo = random.randint(1, 3) 
        if randNo == 1:
            comp = 'S'
        elif randNo == 2:
            comp = 'P'
        elif randNo == 3:
            comp = 'K'
        print(f"Computer chose {comp}")
        print(f"You chose {you}")
        a = gameWin(comp, you)
        if a == None:
            print("The game is a tie!")
        elif a == True:
            print("You Win!")
        else:
            print("You Lose!") 
        quit = input("Wanna play again? Enter - Y else enter - N : ") 
    print("\n------------------------------------------------ GAME OVER ------------------------------------------------")      


# Quiz Game
def quiz():
    print("\n------------------------------------------------ QUIZ GAME ------------------------------------------------")
    a=input("\n\nEnter the category you want to play for [ Sports, Geography, Science ] : ")

    score = 0

    if a.lower() == "geography":
        # Geography
        # Question 1
        print("\n\nQ-1 What is the capital of India?")
        answer = input("ANS: ")
        if answer.lower() == "delhi":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 2
        print("Q-2 Which is the largest planet in our Solar System?")
        answer = input("ANS: ")
        if answer.lower() == "jupiter":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 3
        print("Q-3 Which is the smallest country in the world?")
        answer = input("ANS: ")
        if answer.lower() == "vatican city":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 4
        print("Q-4 Where the Amazon Forest is located?")
        answer = input("ANS: ")
        if answer.lower() == "south america":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect. 👎🏻\n\n")

        # Question 5
        print("Q-5 Which is the nearest planet to the sun?")
        answer = input("ANS: ")
        if answer.lower() == "mercury":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        print("Your final score is " + str(score) + " out of 5.")
        print("\n------------------------------------------------ GAME OVER ------------------------------------------------")


    elif a.lower() == "sports":
        # Sports
        # Question 1
        print("\n\nQ-1 Which is the national sport of India?")
        answer = input("ANS: ")
        if answer.lower() == "hockey":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 2
        print("Q-2 Which cricketer scored 100 centuries in international cricket?")
        answer = input("ANS: ")
        if answer.lower() == "sachin tendulkar":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 3
        print("Q-3 National Sports Day of India is celebrated on whose birthday anniversary?")
        answer = input("ANS: ")
        if answer.lower() == "dhyan chand":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 4
        print("Q-4 In what sport would you use a shuttlecock?")
        answer = input("ANS: ")
        if answer.lower() == "badminton":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 5
        print("Q-5 What is the name of the international men's tennis team competition?")
        answer = input("ANS: ")
        if answer.lower() == "davis cup":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        print("Your final score is " + str(score) + " out of 5.")
        print("\n------------------------------------------------ GAME OVER ------------------------------------------------")

    elif a.lower() == "science":
        # Science
        # Question 1
        print("\n\nQ-1 What is the powerhouse of a cell?")
        answer = input("ANS: ")
        if answer.lower() == "mitochondria":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 2
        print("Q-2 What is the smallest unit of matter?")
        answer = input("ANS: ")
        if answer.lower() == "atom":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 3
        print("Q-3 What is the name of the force that pulls objects towards each other?")
        answer = input("ANS: ")
        if answer.lower() == "gravity":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 4
        print("Q-4 What is the process by which plants make their own food?")
        answer = input("ANS: ")
        if answer.lower() == "photosynthesis":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")

        # Question 5
        print("Q-5 What is the name of the process by which a liquid turns into a gas?")
        answer = input("ANS: ")
        if answer.lower() == "evaporation":
            print("Correct! 👍🏻\n\n")
            score += 1
        else:
            print("Incorrect! 👎🏻\n\n")
            
        print("Your final score is " + str(score) + " out of 5.")
        print("\n------------------------------------------------ GAME OVER ------------------------------------------------")

    else:
        print("Please enter a valid category from the given!") 




print("\n WELCOME TO THE PLAYSTATION 🎮") 
print("\n WHICH GAME YOU WANNA PLAY ?") 
print("\n We have: THE HANGMAN,  STONE-PAPER-KNIFE, QUIZ GAME")  
while True: 
    print("\n Press 1 for THE HANGMAN \n Press 2 for STONE PAPER KNIFE \n Press 3 for QUIZ \n 4 to exit the PLAYSTATION ") 
    pl = input("\nEnter your choice : ")
    if pl == '1': 
        hangman() 
    elif pl == '2': 
        SPK()  
    elif pl == '3': 
        quiz() 
    elif pl == '4': 
        print("\n------------------------------------------------ PLAY STATION SHUTDOWN ------------------------------------------------") 
        break
    else: print("You entered invalid option!")
