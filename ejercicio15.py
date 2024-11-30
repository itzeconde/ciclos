
numero = input("Introduce un número entero: ")
numero=int(numero)

binario = ""  
numero_original = numero 

if numero == 0:
    binario = "0"
else:
   
    while numero > 0:
        residuo = numero % 2  
        binario = str(residuo) + binario  #representa cadena de texto (str)
        numero = numero // 2  
print(f"El número {numero_original} en binario es: {binario}")
