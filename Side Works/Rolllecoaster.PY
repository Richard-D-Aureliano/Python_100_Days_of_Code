height = float(input("What is your height? "))
bill = 0
if height > 120:
    print("You can go on the rollecoaster! ")
    age = int(input("Now, how old are you? "))
    if age < 12:
        bill = 5
        print("Child's ticket are: $5.")
    elif age < 18:
        bill = 7
        print("Teenager's ticket are: $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay! Have a free ride with us.")
    else:
        bill = 12
        print("Adult's ticket are: $12.")
    photo = input("Do you want a photo taken? Y or N ")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")       
else:
    print("You need to get higher first.")
        