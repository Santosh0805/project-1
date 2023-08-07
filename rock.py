import random
print("GAME NAME :- ROCK,PAPER,SCISSORS")
options = ["rock", "paper", "scissors"] 
dic = {"rock":"🗿",
       "paper":"📃",
       "scissors":"✂️"
    }
count_player = 0
count_computer = 0

count_tie=0

running = True
while running:
  player = None
  computer = random.choice(options)
  player_choice = int(
      input('''

      
Do you want to play game!
press 1 : Yes    
press 2 : No
  '''))
  if player_choice == 1:
    while player not in options:
      player = input("_Enter a choice(rock,paper,scissors):")
    print("-Player:",dic[player])
    print("-computer:",dic[computer])
    if player == computer:
      print(" Tie ")
      count_tie+=1
      
    elif player == "paper" and computer == "rock":
      print("Player Winner ")
      print("Computer Lose ")
      count_player+=1
    
    elif player == "rock" and computer == "scissors":
      print("Player Winner ")
      print("Computer Lose ")
      count_player+=1

    elif player == "scissors" and computer == "paper":
      print("Player Winner ")
      print("Computer Lose ")
      count_player+=1
    else:
      print("Player Lose the game ")
      print("Computer Win the game ")
      count_computer+=1
      
  else:
    if count_computer < count_player:
      print("You win")
      print("Computer Lose")
      print("Final score of player =",count_player)
      print("Final score of computer =",count_computer)
      print("------ Thank You For Playing  ------")
    
    elif count_computer > count_player:
      print("Computer Win ")
      print("You Lose ")
      print("Final score of player =",count_player)
      print("Final score of computer =",count_computer)
      print("------ Thank You For Playing  ------")
      
    elif count_computer == count_player:
      print("Final score of player =",count_player)
      print("Final score of computer =",count_computer)
      print("Tie score =",count_tie)
      print("******** Game is Tie ********")
      
      print("------ Thank You ! ------")
    break