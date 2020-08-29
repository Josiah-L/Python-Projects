import random, sys

print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0
rounds = 0

while True:
    print("rounds %s, %s Wins, %s Losses, %s Ties" % (rounds, wins, losses, ties))
    while True:
        rounds += 1
        print("Enter your move: (r)ock (p)aper (s)cissors (q)iut")
        playMove = input()
        if playMove == 'q':
            sys.exit()
        if playMove == 'r' or playMove == 'p' or playMove == 's':
            break
        print("Type one of r, p, s, or q")

    if playMove == 'r':
        print("ROCK versus...")
    elif playMove == 'p':
        print("PAPER versus...")
    elif playMove == 's':
        print("SCISSORS versus...")

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        compMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        compMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        compMove = 's'
        print("SCISSORS")

    if playMove == compMove:
        print("It's a tie!")
        ties += 1
    elif playMove == 'r' and compMove == 's':
        print("You win!")
        wins += 1
    elif playMove == 'p' and compMove == 'r':
        print("You win!")
        wins += 1
    elif playMove == 's' and compMove == 'p':
        print("You win!")
        wins += 1
    elif playMove == 'r' and compMove == 'p':
        print("You lose!")
        losses += 1
    elif playMove == 'p' and compMove == 's':
        print("You lose!")
        losses += 1
    elif playMove == 's' and compMove == 'r':
        print("You lose!")
        losses += 1