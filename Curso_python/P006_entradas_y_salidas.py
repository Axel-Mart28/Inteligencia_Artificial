# pylint: disable=no-member, missing-module-docstring, trailing-whitespace
# En este programa se va a explicar la entrada y salida de datos

print("El resultado", "de sumar", 10, "mas", 50.65, "es:", 10+50.65) # Ejemplo de las propiedades de la palabra print para realizar una suma dentro de este

print("Linea 1\n" + "Linea 2\n" + "Linea 3") #Ejemplo de como se hacen saltos de linea y como se visualizan

nombre = input("Por favor, introduce tu nombre: \n") #Ejemplo sobre como ingrear y pedir datos
print("El nombre almacenado es: " + nombre + ".") #Se muestra el valor introducido en la variable "nombre"

numero_1 = input("Introduce el primer numero a sumar:") #Se pide que el usuario ingrese un numero
numero_2 = input("introduce el segundo numero a sumar:") #Se pide que el usuario ingrese otro numero

suma = numero_1 + numero_2  #Se hace la union de los numeros ingresados y el resultado se guarda en la variable suma
print(suma) # Se muestra el resultado de la variable suma