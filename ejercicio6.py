
numeros =input("¿Cuántos números deseas introducir? ")
numeros=int(numeros)

mayores = 0 
menores= 0  
iguales = 0 

print("Ingresa los números:")
for i in range(numeros):
    numero = input(f"Número {i + 1}: ")
    numero=int(numero)
    if numero > 0:
        mayores+= 1
    elif numero < 0: 
        menores += 1
    else: 
        iguales+= 1


print("\nResultados:")
print("Números mayores que 0:", mayores)
print("Números menores que 0:", menores)
print("Números iguales a 0:", iguales)
