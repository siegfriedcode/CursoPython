#comentario
#if 3 > 5:
#    print('5 es mayor a 3')

#comentario
#if 5 > 3:
#    print('5 es mayor a 3')

x = 5
y = 'chanchito feliz'

#print(x,y)

email = 'chanchito@feliz.com'

#print(email)

mivar = 'chanchito'
mi_var = 'chanchito2'
miVar = 'chanchito3'

a, b, c = 'lala', 'lele', 'lili'

#print(a, b, c)

valor1 = valor2 = valor3 = 'chanchito felíz'

#print(valor1, valor2, valor3)

inicio = 'hola'
final = 'mundo'

#print(inicio+' '+final)
#print(inicio,final)

palabra = 'hola mundo' #string
oracion = "holamundo comilla doble" #string

entero = 20 #integer
conDecimales = 20.2 #float
complejo = 1j #número complejo

#print(palabra, oracion, conDecimales, complejo)

lista = ['hola', 'mundo', 'chanchito feliz']
lista2 = lista.copy()
lista.append('chanchito triste')
#lista.clear()
#print(lista, lista2.count(3))
#print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2 = len(lista2)

#print(largoLista, largoLista2)

#print(lista[0])

# print(lista)
# lista.pop() #esto elimina el último elemento de la lista
# print(lista)
# lista.pop()
# print(lista)

#lista.remove('hola') esto elimina un elemento de la lista por su valor
lista.reverse()
lista.sort()
tupla = ('hola', 'mundo', 'somos', 'tupla')
listaDeTupla = list(tupla)
listaDeTupla.append('chanchito')
#print(listaDeTupla)

rango = range(6)
#print(rango)

diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
    }

# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario['raza'])

#print(diccionario.get('nombre'))

diccionario['nombre'] = 'Fluffy'

#print(len(diccionario))

diccionario['ronronea'] = 'si'

#print(diccionario)
#diccionario.pop('ronronea')
#diccionario.popitem()
#copiaGatito = diccionario.copy()
copiaGatito = dict(diccionario)
#del diccionario['ronronea']
diccionario.clear()
#print(diccionario, copiaGatito)

Fluffy =     {
        "nombre": "Fluffy",
        "edad": 4
    }

Mamba = {
        "nombre": "Black Mamba",
        "edad": 12
    }

gatitos ={
    "Fluffy": Fluffy,
    "Mamba": Mamba
}

print(gatitos)

perritos = dict(nombre = "Chanchito felíz", edad = 6)
print(perritos)

verdadero = True
falso = False

print(verdadero, falso)



