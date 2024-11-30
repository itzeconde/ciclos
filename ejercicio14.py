
n =input("Introduce cuántos números primos quieres mostrar: ")
n=int(n)

contador_primos = 0  
numero = 2          


while contador_primos < n:
   
    es_primo = True
    for i in range(2, int(numero**0.5) + 1): 
        if numero % i == 0:  
            es_primo = False
            break

    if es_primo:
        print(numero, end=" ") 
        contador_primos += 1

    
    numero += 1

print("\n¡Estos son los primeros", n, "números primos!")
