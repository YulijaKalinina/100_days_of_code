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
choices = [rock, paper, scissors]

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
if user_input != "0" and user_input != "1" and user_input !="2":
    print("Type ONLY 0, 1 or 2.")
else:
    computer_choice = choices[random.randint(0,2)]
    user_choice = choices[int(user_input)]
    print(f"Your choice:\n{user_choice}")
    print(f"Computer's choice:\n{computer_choice}")
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == rock and computer_choice == scissors or \
            user_choice == paper and computer_choice == rock or \
        user_choice == scissors and computer_choice == paper:
            print("You win!")
    else:
        print("You lose!")

