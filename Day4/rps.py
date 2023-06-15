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

#Write your code below this line 👇

rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

cmptr = random.randint(0, 2)

if rps == 0:
    print(rock)
elif rps == 1:
    print(paper)
elif rps == 2:
    print(scissors)
else:
    print('Invalid pick.')

print("Computer chose: ")

if cmptr == 0:
    print(rock)
elif cmptr == 1:
    print(paper)
elif cmptr == 2:
    print(scissors)

if rps == cmptr:
    print("Draw")
if rps == 0 and cmptr == 1:
    print("You lose")
elif rps == 0 and cmptr == 2:
    print("You win")
elif rps == 1 and cmptr == 0:
    print("You win")
elif rps == 1 and cmptr == 2:
    print("You lose")
elif rps == 2 and cmptr == 0:
    print("You lose")
elif rps == 2 and cmptr == 1:
    print("You win")
else:
    print("You lose")