'''ciclo while(mientras)
while exp_boleana:
    instrucciones
    actualizacion  de valores '''



num=1
while num<10:
    print(f"hello{num}")
    num=num+5


#mas operadores matematicos
'''n=n+5 ==  n+=5
   n=n-5 ==  n-=5
   n=n*5 ==  n*=5
   n=n/5 ==  n/=5
   '''
#para implementar do while(hacer,hasta) en python

'''while True:
    instrucciones
    if exp_bool:
        break'''

while True:
    option= input("Escribe salir")
    if option == "salir": #para mayusculas
        break