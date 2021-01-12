lista = [12,23,5,29,92,64]

print('Lista original:',lista)

print('\n1. Elimina el ultimo y añadelo al principio')
ultimo = [lista[-1]]
lista = lista[:len(lista)-1]

ultimo[len(ultimo):] = lista
lista = ultimo

# lista.insert(0,lista.pop()) #Opcional
print(lista)

print('\n2. Mueve el segundo elemento a la ultima posicion')
lista.append(lista.pop(1))
print(lista)

print('\n3. Añade el numero 14 al comienzo de la lista')
lista.insert(0,14)
print(lista)

print('\n4. Suma todos los numeros de la lista y añade el resultado al final de la lista')
suma = sum(lista)
lista.append(suma)
print(lista)

print('\n5. Combina la lista actual con la siguiente [4, 11, 32]')
listaB = [4, 11, 32]
lista.extend(listaB)
print(lista)

print('\nElimina todos los numeros impares de la lista')
for n in range(len(lista)-1,-1,-1):
    if lista[n] % 2 != 0:
        lista.pop(n)

print(lista)

print('\nOrdena los numeros de la lista de forma ascendente')
aux = 0
for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux

# lista.sort() #Opcional
print(lista)

print('\nVacia la lista')
for n in range(len(lista)):
    lista.pop()

print(lista)
