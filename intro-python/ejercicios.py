#dato = input('Ingrese dato: ')
#print(data)
#lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

#if lista.count(dato) > 0:
#    print('El dato existe: ', dato)
#else:
#    print('El dato no existe: ', dato)

primero = input('Ingrese primer número: ')

try:
    primero = int(primero)
except:
    primero = False

if(primero==False):
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese segundo número: ')

try:
    segundo = int(segundo)
except:
    segundo = False

if(segundo==False):
    print('El valor ingresado no es un entero')
    exit()

try:
    segundo = int(segundo)
except:
    segundo = False

simbolo = input('Ingrese operación: ')

if simbolo == '+':
    print('Suma: ', primero + segundo)
elif simbolo == '-':
    print('Resta: ', primero - segundo)
elif simbolo == '*':
    print('Multiplicación: ', primero*segundo)
elif simbolo == '/':
    print('División: ', primero/segundo)
else:
    print('El símbolo ingresado no es válido')


#if(primero and segundo):
#    print(primero*segundo)
#else:
#    print('Uno de los valores o ambos, no son números')
    
