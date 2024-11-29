suma = 0  
contador = 0 

print("para este programa debes de ingresar 10 numeros")
while contador < 10:
    numero =input("Ingresa un numero: ")
    numero=int(numero)
    
    suma += numero
    contador += 1  
promedio = suma / 10
print("El promedio de los 10 números  es:", promedio)
