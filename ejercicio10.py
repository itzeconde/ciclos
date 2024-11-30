
base = input("Introduce la base (número real): ")
base=int(base)
exponente = input("Introduce el exponente (entero positivo): ")
exponente=int(exponente)

resultado = 1
if exponente >= 0:
    for _ in range(exponente): 
        resultado *= base
        
    print(f"{base} elevado a la potencia {exponente} es: {resultado}")
else:
    print("El exponente debe ser un número entero positivo.")
