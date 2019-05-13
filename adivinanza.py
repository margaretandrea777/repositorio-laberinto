#juego de adivinar el numero, todos juntos, adivinar un numero generado aleatoriamente,
#ir introduciendo por teclado el dato a adivinar
from random import randint
generado=randint(0,10)
condicion=True
intento=10
while condicion:
    if intento>10:
        numero=input("Dame un numero del 0 al 10")
        intento=intento-1
        if generado==int(numero):
            print("ganaste")
            condicion=False
        else:
            print("perdedor")
            print("te quedan",intento,"intentos")
    else:
        condicion=False
        print("perdicion")