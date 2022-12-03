import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = (rock, paper, scissors)
computer_move = random.choice(choices)


player_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if player_move == 0:
  print(rock)
  if computer_move == paper:
    print("You lose")
  if computer_move == rock:
    print("It's a TIE!")
  if computer_move == scissors:
    print("YOU WIN")
elif player_move == 1:
  print(paper)
  if computer_move == scissors:
    print("You lose")
  if computer_move == paper:
    print("It's a TIE!")
  if computer_move == rock:
    print("YOU WIN")
elif player_move == 2:  
  print(scissors)
  if computer_move == rock:
    print("You lose")
  if computer_move == scissors:
    print("It's a TIE!")
  if computer_move == paper:
    print("YOU WIN")

choices = (rock, paper, scissors)
computer_move = random.choice(choices)
print(f"Computer chose: {computer_move}")