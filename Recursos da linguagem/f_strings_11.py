# Formatação de strings

nome = 'Rodrigo'
altura = 1.73
dinheiro = 5000.48

linha_1 = f'{nome} tem {altura:.2f}cm de altura' # :.2f -> 2 casas decimais
print(linha_1)
print(f'{dinheiro:,.2f}')