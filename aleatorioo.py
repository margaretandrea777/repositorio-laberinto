#creamos un archivo nuevo
#guardamos en la carpeta del repositorio con la extension .py
#uso de numeros aleatorios
from random import randint #importamos la libreria randit
aleatorio=randint(0,20) #creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio) #imprimimos el nro generados

#escribir una funcion sorteo() que reciba una lista de participantes, y elegir a uno de
#los participantes aleatoriamente, y retornar esa persona elegida y que no se vuelva
#a retornar una persona ya sorteada
from random import randint  #importamos la funcion randit de la libreria random
participan=["la","le","li","lo","lu"]  #creo mi lista
def sorteo(participantes): #hago mi funcion llamada sorteo y le tiro un parametro
#x "participantes"
    cant=len(participan)-1 #utilizamos len para saber la cantidad de personas que hay
#en la lista y guardamos en la varible cant y le resto 1 para que no salga del rango
    indice=randint(0,cant)  #generamos un indice aleatorio
    elegido=participan[indice]  #seleccionamos un participante de la lista y guardamos
#en la variable"elegido"
    return elegido  #retorno esa variable
necesidad=sorteo(participan) #le llamo a esa variable y ya
print(necesidad)

 

