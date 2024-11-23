'''
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.

Para este problema se requiere de un acumulador y un contador

Contador: Variable que va, como su nombre lo indica, contando elementos (iteraciones),
por cada iteración el contador va incrementando en 1

Ejemplo:
contador = 0
for i in range(5):
    contador = contador + 1
print(contador)

Acumulador: Variable que va, como su nombre lo indica, acumulando valores en cada iteración,
por cada iteración al valor inicial se le suman nuevos valores al acumulador

Ejemplo:
acumulador = 0;
for i in range(5):
    acumulador = acumulador + i
print(acumulador)

'''
suma=0
acumulador=0

numero=input("Ingresa un numero")
numero=int(numero)
print("NOTA: EL PROGRAMA SE DETINE SI INGRESAS 0")

while numero != 0:
   suma += numero
acumulador+=1

if acumulador==0:
media=0

else:
media=suma/acumulador

print("la suma es",suma)
print("la media es",media)   