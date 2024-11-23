'''ciclo for en python
perimite realizar una serie de instrucciones una cantidad determinada de veces

estructura:
for i in (1...n)

range(fin)
    range(3)   ¨(0,1,2) 
    range(inicio,fin) 
    range (4,7)  (4,5,6)
    range(inicio, fin, pasos)
    range(2,9,2) [2,4,6,8]'''

#ejemplo imprimir los numeros del 1 al 10

for i in range(10):
    print(f"Num {i+1},vuelta {i}")

    #ejemplo imprimir los numeros del 10 al 20
    for i in range(10, 21):
        print(f"Num:{1}")
 #ejemplo imprimir los numeros del 0 al 20
for i in range(0,21,2):
     print (f"{i}")

 #ejemplo imprimir la tabla de multiplicar de un numero leido desde el usuario

     num = input("tabla:")
num=int(num)

for num in range(11):
    resutaldo=num ** i
    print("La taba de multip0licar es num * ")