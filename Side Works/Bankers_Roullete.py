import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#O que encontrei:

names = random.sample(names, 1)
print(f"{names[0]} is going to buy the meal today!")

#random.choice é a opção mais simples;
#Opção dada na aula:

'''num_itens = len(names)

random_choice = random.randint(0, num_itens - 1)

print(f"{names[random_choice]} is going to buy the meal today!")'''
