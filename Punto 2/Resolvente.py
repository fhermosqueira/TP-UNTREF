import math

a = float(input('Ingrese el valor para a: '))
b = float(input('Ingrese el valor para b: '))
c = float(input('Ingrese el valor para c: '))

calcInRaiz = b * b - 4 * a * c

if calcInRaiz < 0:
    print('la ecuación no tiene soluciones reales')
    
else:
    raiz = math.sqrt(calcInRaiz)
    
    x1 = (-b + raiz) / (2 * a)
    if calcInRaiz != 0:
        x2 = (-b - raiz) / (2 * a)
        print('Las soluciones son ' + str(x1) + ' y ' + str(x2))
    else:
        print('La solución es x = ' + str(x1))
        
        

