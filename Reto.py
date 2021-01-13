a = [12,23,5,29,92,64]
print('Lista en su forma normal:', a)
b = a.pop() 
print('Ultimo elemento eliminado: ', b)
a.insert(0, b)
print('Insertado al inicio: ', a)
c = a.pop(1)
print('Elemento posicion 2 eliminado: ',c)
a.append(c)
print('Elemento Agregado al final: ', a)
a.insert(0,14)
print('Agregar elemento 14: ', a)
suma = 0
for i in a:
    suma += i
print('Sumatoria del array: ', suma)
a.append(suma)
print('Agregar resultado de suma al final: ', a)
a +=  [4,11,32]
print('Unir dos listas: ', a)
for i in a[:]:
    if i % 2 == 1:
        a.remove(i)
print('Lista sin numeros pares:', a)  
a.sort()
print('Lista Ordenada de forma ascendente: ', a)
a.clear()
print('Lista Vacia', a)