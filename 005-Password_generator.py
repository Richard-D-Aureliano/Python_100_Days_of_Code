import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'ç', 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ç']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
letter_choice = int(input("How many letter's do you want in your password?\n"))
number_choice = int(input("And how many numbers?\n"))
symbol_choice = int(input("And how many symbols?\n"))

total1 = 1
total2 = 1
total3 = 1
password = [""]

for x in letters:
    if letter_choice != 0:
        if total1 <= letter_choice:
            total1 += 1
            password.append(random.choice(letters))

for x in numbers:
    if number_choice != 0:
        if total2 <= number_choice:
            total2 += 1
            password.append(random.choice(numbers))

for x in symbols:
    if symbol_choice != 0:
        if total3 <= symbol_choice:
            total3 += 1
            password.append(random.choice(symbols))

random.shuffle(password)
password = "".join(password)
print(f"Your password is:\n{password}")
