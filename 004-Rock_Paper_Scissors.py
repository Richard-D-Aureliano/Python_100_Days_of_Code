import random
rock ='''    
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
game = [rock, paper, scissors]
decision = int(input("What do you choose? Type 0 fo Rock, 1 for Paper or 2 for Scissors: "))
if decision >=3 or decision <0:
    print("Wrong key. You lose.")
else:
    print(f"Your decision is: {decision}\n{game[decision]}")
    number = random.randint(0,2)
    computer = (game[number])
    print(f"Computer chose:\n{computer}")
    if decision == 0 and number == 2:
        print("You win!")
    elif decision == 2 and number == 0:
        print("You Lose!")
    elif decision > number:     
        print("You win!") 
    elif decision < number:    
        print("You Lose!")
    elif decision == number:
        print("It's a draw!")
