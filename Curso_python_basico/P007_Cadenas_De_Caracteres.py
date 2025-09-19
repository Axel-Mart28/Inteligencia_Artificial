# pylint: disable=no-member, missing-module-docstring, trailing-whitespace
# En el siguuente programa se muestran ejemplos de la concatenacion de caracteres

fragmento1 = "La programacion es como la vida:"  #Primer fragmento de la palabra
fragmento2 = " Llena de errores, pero tambien de posibilidades." #Segundo fragmento de la palabra

frase_completa = fragmento1 + fragmento2 #Se hace la concatenacion (union de ambos fragmentos) y se guarda el resultado en la variable "frase_completa"
print(frase_completa)  # Se muestra el resultado, en este caso la palabra completa

#Diferentes maneras de mostrar la siguiente cadena de caracteres: "El tiempo es oro, me dijo"

print('"El tiempo es oro", me dijo') 

print("\"El tiempo es oro\", me dijo.")

nombre = input("Por favor, introduzca su nombre: \n") #Se declara la variable nombre, y va a guardar lo que se introduzca
print(f"Hola, {nombre}. Tenga un maravilloso dia.") #"(f) permite hacer una técnica para poder poner el valor de una variable, y se pone entre llaves"

PI = 3.1416  #Se declara la variable PI y se le asigna el valor de PI
print(f"El valor de PI siempre sera {PI}.") #Se imprime el valor de la variable PI