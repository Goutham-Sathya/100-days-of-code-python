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

game_images = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# Validate input early and quit if invalid
if not user_choice.isdigit() or int(user_choice) not in [0, 1, 2]:
    print("Invalid input. You lose!")
    exit()

user_choice = int(user_choice)
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Define winning conditions explicitly
# Each tuple (winner, loser)
winning_combinations = [(0, 2), (1, 0), (2, 1)]

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice, computer_choice) in winning_combinations:
    print("You win!")
else:
    print("You lose!")
