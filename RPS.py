com_scr = 0
pla_scr = 0
winning_scr = 5
while com_scr < winning_scr and pla_scr < winning_scr:
    p1 = input ("Please input rock/paper/scissors: ")
    if p1 == "quit" or p1 == "q":
       break
    import random
    # Generates a random number between
    # a given positive range
    r1 = random.randint(0, 2)
    if r1 == 0:
        r1 = "rock"
    elif r1 == 1:
        r1 = "paper"
    elif r1 == 2:
        r1 = "scissors"
    p2 = r1
    print("The Computer gives " + r1)
    if p1 == "rock" and p2 == "scissors":
        print("Player 1 WINS")
        pla_scr += 1
    elif p1 == "paper" and p2 == "rock":
        print("Player 1 WINS")
        pla_scr += 1
    elif p1 == "scissors" and p2 == "paper":
        print("Player 1 WINS")
        pla_scr += 1
    elif p2 == "rock" and p1 == "scissors":
        print("Computer WINS")
        com_scr += 1
    elif p2 == "paper" and p1 == "rock":
        print("Computer WINS")
        com_scr += 1
    elif p2 == "scissors" and p1 == "paper":
        print("Computer WINS")
        com_scr += 1
    elif p1 == p2:
        print("Nobody WINS")
    print(f"Human:{pla_scr} Computer:{com_scr}")            
if pla_scr > com_scr :
    print("The Human Rules!")
elif pla_scr == com_scr:
    print("It's a tie")
elif pla_scr < com_scr :
    print("Skynet Rules!")
        
