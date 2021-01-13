
correo= input('Ingrese su correo electronico: ')
def validar(correo):
    if "@" in correo:
        return True
    else:
        return False
res = validar(correo)

if res:
    print('Correo Valido')
else:
    print('Correo no valido')


numero = int(input('Ingrese un numero: '))

def primo(numero):
    if numero < 1:
        return False
    elif numero  == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return True
            else:
                return False
            
resultado = primo(numero)

if resultado:
    print('Numero Primo')
else:
    print('Numero no es primo')

