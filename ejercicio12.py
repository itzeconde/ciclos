
total_ahorrado = 0
for mes in range(1, 13): 
    mensual = input(f"Introduce el ahorro de el mes {mes}: ")
    mensual=int(mensual)
    
    total_ahorrado += mensual
    
    print(f"Lo que haz ahorrado en el mes {mes}: {total_ahorrado:.2f} euros")

print(f"\nEl total ahorrado en el año es: {total_ahorrado:.2f} euros")
