import calculator_art


# add
def add(a, b):
    return a + b


# subtract
def sub(a, b):
    return a - b


# multiply
def mul(a, b):
    return a * b


# divide
def div(a, b):
    return a / b


operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculation():
    print(calculator_art.logo)
    num1 = float(input("Type in the first number: "))
    for operator in operation:
        print(operator)

    should_continue = True

    while should_continue:
        option = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operation[option]
        answer = calculation_function(num1, num2)
        print(f"{num1} {option} {num2} = {answer}")

        if input(f"Do you wanna continue with {answer}? Type 'y' or 'n': ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculation()


calculation()
