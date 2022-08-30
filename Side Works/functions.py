def format_name(first, last):
    if first == "" or last == "":
        return "You did't provide any valid inputs."
    f_name = first.title()
    l_name = last.title()
    return f"{f_name} {l_name}"


first_name = input("Tell me your first name: ")
last_name = input("Tell me your last name: ")


print(format_name(first=first_name, last=last_name))
