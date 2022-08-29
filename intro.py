
''' Este es un supercomentario
    de inicio a nuestro resumen 
''' 
#====================
# Operaciones básicas
#====================
print (2+3)
print (2*3)
print (2/3)
print (2**10) # raíz cuadrada
print (2**0.5)
print (10%2)
print (19%0.1) # esclusivo en pyton

#=========================================
# Para saber el tipo de objeto se usa type
#=========================================
t=0
print(type(t)) # entero
t=3.6
print(type(t)) # real (flotante)
t=True
print(type(t)) # booleano (bool)

#==================
#Mensaje a pantalla
#==================
print ("Este es un comando de python. ", "Este es otro enunciado.",t)
print('id:',1)
print('First NAme:','Steve')
print('Last Name: ','JObs')
print("VAmos a sumar esto" + " con esto otro")

#==============================================
# Continuar una instrucción en varios renglones
#==============================================
if 100 > 99 and \
   200 <= 300 and \
True != False:
   print('Hello World!')
#======================================
# Comandos diferentes en la misma línea
#======================================
print("Hola"); print("tu!!")   # Se considera mala práctica
#================================================
# Usando paréntesis redonodos, cuadrados o llaves 
# se puede escribir en varios renglones
#=================================================

list = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [ [1,2,3,4 ],[5,6,7,8],[9,10,11,12] ]

print(list)
print(matriz)

#==================================================================
# Indentación estricta para procesos dependientes de : (dos puntos)
#==================================================================
if 10>5: 
  print ("diez es mayor que cinco")
  print("otra indentación") 
for i in list:
   print (i)
   print("ok")
if 10>5:
 print("verdadero")
 if 10<20:
    print("verdadero")
elif 5>3: # comienza segundo condicional 
  print ("eso no se imprimira")
else:
   print ("aquí nunca llega")

#=================
# FUnciones 
#================
def say_hello(name):
    print("hello ",name)
    print("Welcome to phynton tutorials")

say_hello("Julián")

#==================================================
# Input permite obtener datos del usarioen prompter
#==================================================
nombre = input ("Dame tu nombre: ")
print("Hola como estás",nombre)

#==================================================
# Los enteros son de precisión ilímitada
#==================================================
y = 5000000000000000000000000000000000
print(y)

#===========================================================
# Se puede delimitar números con guión bajo pero no con coma
#============================================================
y=5_000_000
print(y)

#===================================================
# La función int() cambia strings y floats a enteros
#===================================================
numero = int(input("Dame tu edad: "))
type(numero)

#====================================================
# LA notación científica de flotantes utiliza e o E
#======================================================
# 1.2 x 10^{-9}
#==============
print(y)

#=========================================================
# La funcion float() convierte strings y enteros a floats 
#=========================================================
y = float("14.3")
print(y)

#==========================================================
# Los complejos se escribren con la raíz de menos uno 
# j siempre con un número como prefijo 
# no acepta la j suelta
#===========================================================
z= 1+1j

# suma + 
# resta -
# multiplicación *
# división /
# módulo %
# exponente **
# // funcion piso 
# Funciones para transfomrar números int() float() complex()
# Operaciones abs() round() pow()

print(round(3.14159,4))

#=========================
# Strings de varias líneas
#=========================
parrafo= """ En el bosque de la china la chinita se perdió"""
print(parrafo)

#==============================================
# La función len() obtiene el tamaño del string
#==============================================
n=len(parrafo)
print(n)

#==============================================================
# Las letras es un string ocupan lugares como en un arreglo
# (también de atrás para adelante comenzando en -1 el último)
#===============================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])

