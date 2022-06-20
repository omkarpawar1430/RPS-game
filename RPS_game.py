# RPS Game
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


import random
game_pics = [rock, paper, scissors]
your_choice = int(input("choose your action: for Rock - 0, for Paper - 1, for Scissors - 2 "))
print("You choose")
image_yc = game_pics[your_choice]
print(image_yc)
computer_choice = int(random.randint(0, 2))
print("computer choose")
image_cc = game_pics[computer_choice]
print(image_cc)
print("Result:")

if your_choice >= 3 or your_choice < 0:
  print("you choose wrong number.")
elif your_choice == computer_choice:
  print("It's a Draw.")

elif your_choice == 0 and computer_choice == 2:
  print("You win.")
elif your_choice == 2 and computer_choice == 1:
  print("You win.")
elif your_choice == 1 and computer_choice == 0:
  print("You win.")
else:
  print("You lost.")
