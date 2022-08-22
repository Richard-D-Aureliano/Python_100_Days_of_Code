# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Podemos Cocatenar os dois nomes para fazer tudo isso apenas uma vez
name1 = name1.lower()
name2 = name2.lower()
true1 = sum(map(name1.count, ["t", "r", "u", "e"]))
true2 = sum(map(name2.count, ["t", "r", "u", "e"]))
love1 = sum(map(name1.count, ["l", "o", "v", "e"]))
love2 = sum(map(name2.count, ["l", "o", "v", "e"]))

truex = true1 + true2
lovex = love1 + love2
final = str(truex) + str(lovex)
final = int(final)

if final <= 10 or final >=90:
    print (f"Your score is {final}, you go together like coke and mentos.")
elif final >=40 and final <=50:
    print (f"Your score is {final}, you are alright together.")
else:
    print (f"Your score is {final}.")

#Esse me deu um trabalhinho pra encontrar a solução com o SUM e MAP;