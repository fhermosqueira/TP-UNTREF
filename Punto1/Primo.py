def primo(num):
    if num <= 1:
        return False  
    if num == 2:  
        return True  
    if num % 2 == 0:
        return False  
    for i in range(3, num):  
        if num % i == 0:  
            return False  
    return True  

print('Ingrese un número:')
num = int(input())
if primo(num):
    print('es primo')
else:
    print('no es primo')