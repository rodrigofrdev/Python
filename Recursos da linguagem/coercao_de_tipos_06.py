# Converter um tipo em outro tipo

# Python usa polimorfismo para lidar com tipos diferentes para o mesmo operador
print(1 + 1)
print('a' + 'b')
# print('1' + 1) # TypeError: can only concatenate str (not "int") to str

print(int('1'))
print(float('1'))
print(str(1))
print(bool(1))