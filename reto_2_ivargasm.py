"""
1.- Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".

2.-Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.
"""
import re
"""
#1
##### esta funcion solo valida que exista un @ para validar el email
def valid_email(email):
    if "@" in email:
        print(f"tu email: {email} es valido")
    else:
        print(f"tu email:ismael@corre {email} no es valido")


##### Esta funcion evalua por medio de una exprecion regular la valides de un correo incluyendo que despues del @ exista un ".com, .mx, ..."
def valid_mail_expreg(email):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',email.lower()):
    	print(f"tu email: {email} es valido")
    else:
        print(f"tu email:ismael@corre {email} no es valido")


email = input('Ingresa un email: ')

valid_email(email)
valid_mail_expreg(email)
"""

#2
def primo(numero):
    primo=0
    if numero > 0:
        for i in range(1,numero+1):
            if numero%i == 0:
                primo += 1
        if primo > 2:
            print('El numero: {0} no es primo'.format(numero))
        else:
            print('El numero {0} es primo'.format(numero))
    else:
        print('Ingresa un numero mayor a 0')

try:
    numero = int(input('Ingresa un numero: '))
except ValueError:
    print('Ingresa un dato numerico')

primo(numero)

