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

moves = [rock, paper, scissors]
you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(moves[you])
opponent = random.randint(0,2)
print(f"Computer chose:\n{moves[opponent]}")

if you == opponent:
    print("It's a draw.")
elif you == 0 and opponent == 2:
    print("You win!")
elif you == 1 and opponent == 0:
    print("You win!")
elif you == 2 and opponent == 1:
    print("You win!")
else:
    print("You lose!")