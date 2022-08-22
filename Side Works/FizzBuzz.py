#Números de 1 a 100, se o número for divisível por 3, print Fizz
#Se for divisível por 5 , print Buzz. Se for por ambos, print FizzBuzz

for x in range(1,101):
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)