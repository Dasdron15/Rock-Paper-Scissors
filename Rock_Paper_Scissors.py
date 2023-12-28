import random
import time

choosing = ["R", "P", "S"]
points = 0
opponent_points = 0
thinking_time = random.randint(1, 3)


def system():
    global opponent_points, points, ending
    if choice == "R" and opponent == "P":
        opponent_points += 1
        ending = "Opponent won!"
    elif choice == "P" and opponent == "S":
        opponent_points += 1
        ending = "Opponent won!"
    elif choice == "S" and opponent == "R":
        opponent_points += 1
        ending = "Opponent won!"
    elif choice == "R" and opponent == "S":
        points += 1
        ending = "You won!"
    elif choice == "P" and opponent == "R":
        points += 1
        ending = "You won!"
    elif choice == "S" and opponent == "P":
        points += 1
        ending = "You won!"
    elif choice == opponent:
        ending = "It's a draw"


def main():
    global choice, opponent, ending
    rounds = int(input("how many rounds do you want to play?: "))
    round_var = rounds

    for k in range(rounds):
        opponent = random.choice(choosing)
        choice = input("Rock Paper or Scissors? R/P/S: ")
        system()

        for i in range(thinking_time):
            print("\rOpponent is thinking...", end="")
            time.sleep(0.4)
            print("\rOpponent is thinking.. ", end="")
            time.sleep(0.4)
            print("\rOpponent is thinking.  ", end="")
            time.sleep(0.4)
            print("\rOpponent is thinking   ", end="")
            time.sleep(0.4)

        print("")
        print(f"Opponent chose {opponent}")
        time.sleep(1)
        print(ending)
        time.sleep(0.5)
        print(f"""Your points - {points}
Opponent points - {opponent_points}""")
        time.sleep(0.5)
        round_var -= 1
        print(f"{round_var} rounds left")
        time.sleep(0.3)

main()

again = input("Do you want to play again? Y/N: ")

if again == "Y" or again == "y" or again == "yes" or again == "Yes" or again == "YES":
    points = 0
    opponent_points = 0
    main()
elif again == "N" or again == "n" or again == "no" or again == "No" or again == "NO":
    print("See you next time)")
    exit()
