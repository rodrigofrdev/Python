# AND, OR, NOT

choice = input("[E]nter or [L]eave: ")
password = input("Type the password: ")
password_allowed = "123456"

# Se a primeira condição for verdadeira, a segunda condição será verificada
# Se a primeria condição for falsa, a segunda condição não será verificada
if (choice == "E" or choice == "e") and password == password_allowed:
    print("You entered on the system")
else:
    print("You left the system")

#  Avaliação curto-circuito
print(True and 0 and False)
print("" and 1 and True)

print(not True)
print(not False)