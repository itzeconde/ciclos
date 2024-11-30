'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''
while True:
    inferior = input("Introduce el límite inferior del intervalo: ")
    inferior=int(inferior)
    superior = input("Introduce el límite superior del intervalo: ")
    superior=int(superior)
    
    if inferior < superior :
        break 
    else:
        print("El límite inferior no debe ser mayor que el superior.")

suma = 0  
numeros_fuera = 0  
limite_igual = False

print("Introduce los números (introduce 0 para terminar):")
while True:
    numero = int(input("Introduce un número: "))
    
    if numero == 0:
        break  
    if inferior < numero < superior:
        suma += numero  
    else:
        numeros_fuera += 1 

    if numero ==inferior or numero == superior:
        limite_igual = True


print("La suma de los números dentro del intervalo es:", suma)
print("Cantidad de números fuera del intervalo:", numeros_fuera)
if limite_igual:
    print("Se ha introducido un número igual a uno de los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites.")
