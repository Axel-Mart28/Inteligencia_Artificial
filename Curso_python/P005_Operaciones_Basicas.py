# pylint: disable=no-member, missing-module-docstring, trailing-whitespace

"En el siguiente programa se muestra un ejemplo de las operaciones matematicas basicas en python"

print(20 + 100) #Aqui, se imrpime en la consola el resultado de la operacion entre parentesis

operacion = 20 + 50 # Se declara una variable llamada "operacion" la cual guarda el valor de la operacion de suma
print(operacion)#Imprime el resultado de la variable

operacion_resta = 10 - 4 #Se declara una variable llamada "operacion_resta" la cual guarda el valor de la operacion de resta
print(operacion_resta)#Imprime el resultado de la variable

operacion_mult = 10 * 4 #Se declara una variable llamada "operacion_mult" la cual guarda el valor de la operacion de multiplicacion
print(operacion_mult)#Imprime el resultado de la variable

operacion_division = 25 /5 #Se declara una variable llamada "operacion_division" la cual guarda el valor de la operacion de division
print(operacion_division)#Imprime el resultado de la variable

"Ejemplo con operaciones mixtas:"
operacion_mixta = 100 * 2 + 8 / 4 - 9 + 7 * 14 * 5
print(operacion_mixta)#Imprime el resultado de la variable

numero1 = 100
numero2 = 400

resultado = numero1 + numero2

print(resultado)

numero3 = 10
numero4 = 3

cociente = numero1 / numero2 #Division normal de los valores de las variables 
resto = numero1 % numero2  #Division modulo, que devuelve el residuo de la division
division_entera = numero3 // numero4  #Division que devuelve un resultado entero

print("Cociente:", cociente)
print("Residuo:", resto)
print("division_entera:", division_entera)


#Programa para calcular la media de edades:

#Lista con edades:
edades = [15, 26, 54, 22, 17, 50, 33, 32]

#Obtener la suma de las edades:
suma_edades = sum(edades)

#Obtener el numero total de edades (cuenta los valores de la lista):
numero_edades = len(edades)

#Calcular la media:
media = suma_edades / numero_edades

#Imprimir resultados:
print("En total hay:", numero_edades, "edades")
print("La edad media de todas ellas es:", media)

#Calculo de 2 elevado a la 3:
operacion_potencia = 2**3
print("El resultado  de la optencia es: ", operacion_potencia)

#Calculo con parentesis:
operacion_parentesis = (10 + 6) *2
print("El resultado de la operacion por Jerarquia es:", operacion_parentesis)

#Representar numeros grandes con decimal:
numero_largo = 56_404_327_843.78
print("El resultado del numero grande en decimal es:", numero_largo)





