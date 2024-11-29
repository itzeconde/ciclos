
numero1 = input("Introduce el primer número: ")
numero1=int(numero1)
numero2 = input("Introduce el segundo número: ")
numero2=int(numero2)

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print(f"Números pares entre {numero1} y {numero2}:")
for numero in range(numero1, numero2 + 1):  
    if numero % 2 == 0: 
        print(numero)
