import random

def addHumanPoint():
    global humanPoints
    humanPoints += 1
    print("Human Points ", humanPoints)

def addComputerPoint():
    global computerPoints 
    computerPoints += 1
    print("Computer Points ", computerPoints)

def addDrawPoint():
    global tiePoints
    tiePoints += 1
    print("Draw Points ", tiePoints)
    
def computerChoice():
    choices = ("rock","paper","scissors")
    randomChoices = random.choice(choices)
    return randomChoices

def gameLogic(x):
    if humanSelection == "rock" and computerSelection == "scissors":
        print("You win " + humanSelection + " beats " + x)
        return addHumanPoint()
    elif humanSelection == "paper" and computerSelection == "rock":
        print("You win " + humanSelection + " beats " + x)
        return addHumanPoint()
    elif humanSelection == "scissors" and computerSelection ==  "paper":
        print("You win " + humanSelection + " beats " + x)
        return addHumanPoint()
    elif humanSelection == computerSelection:
        print("This is a draw " + humanSelection + " & " + x)
        return addDrawPoint()
    else:
        print("You lose " + humanSelection + ", can't beat " + x)
        return addComputerPoint()
    
def humanChoice():
    humanInput = input("Enter rock, paper or scissors: ", ).lower()
    print(humanInput)
    if humanInput == "rock" or humanInput == "paper" or humanInput == "scissors":
        return humanInput
    else:
        print(humanInput, "is not a valid choice. Please try again.")
        return humanChoice()

def getWinner():
    if humanPoints > computerPoints:
        print("Congrats you win")
    elif computerPoints > humanPoints:
        print("HAHAHA you lost loser!")
    elif humanPoints == computerPoints:
        print("Draw game")

tiePoints = 0
humanPoints = 0
computerPoints = 0
i = 0    
while i < 6:
    humanSelection = humanChoice()
    computerSelection = computerChoice()
    game = gameLogic(computerSelection)
    i += 1

getWinner()




