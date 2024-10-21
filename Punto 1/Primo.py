def primo(num):
    if num <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    if num == 2:  
        return True  # El 2 es el único número primo par
    if num % 2 == 0:
        return False  # Si es par y mayor que 2, no es primo
    for i in range(3, num):  # Revisa divisores desde 3 hasta n-1
        if num % i == 0:  
            return False  # Si encontramos un divisor exacto, no es primo
    return True  # Si no se encontró ningún divisor, es primo

print('Ingrese un número:')
num = int(input())
if primo(num):
    print('es primo')
else:
    print('no es primo')