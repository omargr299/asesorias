'** PRIMERA IMPRESION **'
print("Hola")

#nota: PRINT funcion que permite mostrar datos en la consola

'** SECUENCIAS DE ESCAPE **'
print("Hola\"")
print('\'')
# nota: en un string no se pueden usar caracteres especiales como \ ' " ( ) si una barra invertida por que da error

print("hola\nMi\nNombre\nEs\nOmar\n\n")

print("Hola\tComo estas") 
#estas secuencias generan una accion especial en el string

'** TIPOS DE DATOS **' 
variable = 10
print(variable)

# datos guardados en variables
enteros = 10
flotantes = 3.14
string = "hola"
string_2 = "8jkgvkjbvjvjlkl"
boleano = True
booleano_2 = False
print(enteros)
print(flotantes)
print(string)
print(boleano)
print(booleano_2)

# mostramos el tipo de dato con la funcion TYPE
print( type(enteros) )
print( type(flotantes) )
print( type(string) )
print( type(string_2) )
print (type(boleano) )
print( type(booleano_2) )

'** OPERADORES ARITMETICOS **'
'suma'
print(5+3)
print(2.13+3.14)
print(5.4+3)
'print(3+"9")' #nota si se suma un numero con strign genera error (igual con las demas operaciones)
print(True+True)
print(3+True)
print("Hola" + "como estas")

'resta'
print(4-2)

'multiplicacion'
print(6*3)
print("hola"*4)

'division' #division con decimal
print(8/2)

'division entera' #division sin decimal
print(5//2)

'modulo' #resto de una division antes del punto decimal
print(8%2)
print(5%2)

'exponencial'
print(4**2)

' OPERADORES DE ASIGANCION '
#forma resumida para hacer una operacion con el valor de una variable y remplazarlo con el enuevo valor
#es decir toma el valor de la variable, le hace la operacion y guarda el nuevo valor en la variable
numero = 13
print(numero)
numero += 1
print(numero)
numero -= 1
print(numero)
numero *= 2
print(numero)
numero /= 2
print(numero)
numero %= 2
print(numero)
numero **= 2
print(numero)

'** ENTRADAS **'
# input pideun dato al usaurio por medio de la consula
respuesta = input("Ingresa un dato:") # el emnsaje entre parentesis es el mensaje que se muestra antes de pedir el dato

print("El numero es:",respuesta)

'** TEMPLETES **'
# Los templetes son una forma rapida de remplazar valores en un string

respuesta = input("Ingresa un dato:")
otro_numero=11

# diferentes formas de mostrar las variables
print("El numero es:", respuesta, " y el otro numero es: ", otro_numero)
print("El numero es: {} y el otro numero es: {}".format(respuesta, otro_numero))
print(f"El numero es: {respuesta} y el otro numero es: {otro_numero}")

' PEDIR DATOS DEL TIPO CORRECTO '
# int() transforma un dato a entero
# float() transfofrma un dato a flotante
# str() transforma un dato a string (el input guarda el dato como string por defecto)
n = int(input("Ingresa un numero: "))
n = int("Hola")
print(type(n))

'** ESTRUCTURAS DE CONTROL**'

'* IF *'
# el IF realiza ciertas intrucciones cuando recibe un valor TRUE
if True:
    print("esta en el if")

# FALSE no deja ejecutar las instrucciones adentro del IF
if False:
    print("entro en el segundo if")

'* OPERADORES RELACIONALES *'
# Comparan datos y regresan un valor booleano (TRUE o FALSE)
print(1==1) # igual que
print(0<1) # menor que
print(2>1) # mayor que
print(0<=1) # menor o igual que
print(2>=1) # mayor o igual que
print(1!=1) # diferente de

numero = int(input("Ingresa un numero: "))

'* ELSE y ELIF *'
# si la el IF es TRUE ejecuta las instrucciones que estan dentro de el
# de lo contrario revisara las condiciones de los ELIF hasta encontrar el que te condicion que sea cierta
# en caso de que ninguna sea cierta ejecutara las acciones del ELSE sin imporatar niguna condicion
if numero==1:
    print("Es un uno")
elif numero==2:
    print("Es un dos")
elif numero==3:
    print("Es un tres")
else:
    print("No lo conozco")

print("Termino el programa")

numero = int(input("Ingresa un numero: "))

' forma resumida '
# cuando solo tenemos un instruccion podemos acomodar los IF´s en una sola linea
if numero==1: print("es un uno")
elif numero==2: print("Es un dos")
elif numero==3: print("Es un tres")
else: print("No lo conozco")

'* OPERADOR TERNARIO *'
numero = int(input("Ingresa un numero: "))

# forma en que podemos resumir el IF y el ELse con una sola instruccion en un simple linea
# se lee:
# IMPRIME "Es un uno " SI el Numero es igual a 1 DE LO CONTRARIO IMPRIME "No lo conozco"
print("Es un uno") if numero==1 else print("No lo conozco")