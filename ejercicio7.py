'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''
print("Introduce caracteres:")

while True:
    caracter = input("Ingresa un carácter: ") 

    if caracter == " ":
        print("Fin del programa.")
        break 

    if caracter in "aeiouAEIOU": 
        print("VOCAL")
    else:
        print("NO VOCAL")
