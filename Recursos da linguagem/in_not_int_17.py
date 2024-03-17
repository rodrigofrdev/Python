# in e not in é aplicado em iteráveis

name = input("Type your name: ")
search_letter = input("Type a letter: ")

if search_letter not in name:
    print(f"The letter {search_letter} is not in the name {name}")
else:
    print(f"The letter {search_letter} is in the name {name}")