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

import random

choose = int(input("What do u chose? Type 0 for rock, 1 for paper or 2 for scissor."))

list_choices = [rock, paper, scissors]

print(list_choices[choose])

randon_choiceint = random.randint(0 , 2)
pc_chosen = list_choices[randon_choiceint]


print(f"Computer chose:\n {pc_chosen}")

if choose == 0 and randon_choiceint == 0:
  print("It's a draw")
elif choose == 0 and randon_choiceint == 1:
  print("You lose")
elif choose == 0 and randon_choiceint == 2:
  print("You Won")
elif choose == 1 and randon_choiceint == 0:
  print("You won")
elif choose == 1 and randon_choiceint == 1:
  print("It's a draw")
elif choose == 1 and randon_choiceint == 2:
  print("You lose")
elif choose == 2 and randon_choiceint == 0:
  print("You lose")  
elif choose == 2 and randon_choiceint == 1:
  print("You won")
elif choose == 2 and randon_choiceint == 2:
  print("It's a draw")  

