import  random # This is an example of the random libary

def get_choices(): #This is a function that will contain a block of code that will be executed when it is called. A function is a block
  player_choice = input("Enter a (choice rock ,paper ,scissors)") #This a variable we can store data inside of it and we also have an exmpale of using input
  options = ["rock", "paper", "scissors"] #Exmaple of a list
  computer_choice = random.choice(options)

  choices = {"player":player_choice, "computer":computer_choice} #This is what a dictionary looks like
  return choices #This will return the value for computer_choice#


def checkwin(player, computer): #exmaple of parameters that will be used for an argument
  print(f"You choose {player},  computer choose {computer}" ) #This is an exmaple of a f string
  if player == computer:
    return "Its a tie"
  elif player == "rock":
    if computer =="scissors":
      print("you win")
      return "Rock smashs siccors "
    else:
      return " paper  covers rock  you lose"

  elif player == "scissors":
    if computer == "paper":
      print("you win")
      return "scissors cuts paper"
    else:
      return " rock smashs scissors you lose"
  elif player == "paper":
    if computer == "rock":
      print("you win")
      return "Paper covers Rock"
    else:
      return "scissors cuts paper you lose"

choices = get_choices()

result = checkwin(choices["player"], choices["computer"])

print(result)