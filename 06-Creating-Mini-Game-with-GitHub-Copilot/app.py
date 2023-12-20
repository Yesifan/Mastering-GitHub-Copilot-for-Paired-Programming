# write 'hello world' to the console
print("hello world")


def rock_paper_scissors_game():
    """
    ## The winner of the game is determined by three simple rules:
    - Rock beats scissors.
    - Scissors beat paper.
    - Paper beats rock.

    ## Game interaction considerations

    The computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors). Your game interaction will be through the console (Terminal).

    The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
    At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
    By the end of each round, the player can choose whether to play again.
    Display the player's score at the end of the game.
    The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
    """
    import random

    # create a list of play options
    t = ["Rock", "Paper", "Scissors"]

    # assign a random play to the computer
    computer = t[random.randint(0, 2)]

    # set player to False
    player = False

    while player == False:
        # set player to True
        player = input("Rock, Paper, Scissors? ")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")

        # player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[random.randint(0, 2)]


def rock_paper_scissors_game2():
    """
    Add a scoreboard based on rock_paper_scissors_game func.
    scoreboard like this: player: 1, computer: 2
    show the scoreboard at the each round
    """
    import random

    # create a list of play options
    t = ["Rock", "Paper", "Scissors"]

    # assign a random play to the computer
    computer = t[random.randint(0, 2)]

    # set player to False
    player = False

    # scoreboard
    player_score = 0
    computer_score = 0

    while player == False:
        # set player to True
        player = input("Rock, Paper, Scissors? ")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                computer_score += 1
            else:
                print("You win!", player, "smashes", computer)
                player_score += 1
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                computer_score += 1
            else:
                print("You win!", player, "covers", computer)
                player_score += 1
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                computer_score += 1
            else:
                print("You win!", player, "cut", computer)
                player_score += 1
        else:
            print("That's not a valid play. Check your spelling!")

        # player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[random.randint(0, 2)]

        print(f"player: {player_score}, computer: {computer_score}")


if __name__ == "__main__":
    rock_paper_scissors_game2()
