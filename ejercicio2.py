'''
Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''

import random

aleatorio = random.randint(1, 100)

intentos = 10

print("Adivina el número entre 1 y 100. Tienes 10 intentos.")

while intentos > 0:
    numero = int(input("Introduce un número: "))

    if numero == aleatorio:
        print("¡Felicidades! Has acertado.")
        break
    elif numero < aleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    
    intentos -= 1
    print(f"Te quedan {intentos} intentos.")

if intentos == 0:
    print(f"Perdiste, el número era {aleatorio}.")