programing_dictionary = {
    "Loop": "Do the same thing, over and over again",
    "Bug": "An error of programing that make your program don't work as expected"
}

print(programing_dictionary)

for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])

# Limpa a biblioteca existente:
programing_dictionary = {}

print(programing_dictionary)

# Atribuindo novo valor ou adicionando um novo elemento:
programing_dictionary["loop"] = "What?"

print(programing_dictionary)
