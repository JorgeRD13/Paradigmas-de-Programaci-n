#=================================================
# Conjunto en python 
#=================================================

even_nums={2,4,6,10} # Conjunto de números pares
print(even_nums)

# El bool no es parte del conjunto 
emp = {1,'Steve', 10.5, True} # conjunto de diferentes objetos 
print(emp)

nums = {1,2,2,3,4,4,5,5}
print(nums)

#=================================================
# Convertir secuencia a conjunto 
# No lo genera en orden 
#=================================================

s = set('Hello')
print(s)

s = set((1,2,3,4,5)) # tupla a conjunto 
print (s)

#=================================================
# De diccionario a conjunto: conjunto de llaves
#=================================================

d = {1:'One', 2: 'TWo'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update (nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 #Unión 
print(su)

si = s1&s2 # Intersección 
print(si)

sr = s1-s2 #Diferencia de conjuntos 
print(sr)

sp = s2-s1
print(sp)

ss= s1 

#=================================================
# Uso de diccionarios 
#=================================================

capitals = {"USA":" Washington D.C", "Frances":"Paris", "India":"New Delphi"}
print(capitals)

#=================================================
# llave:valor
#=================================================
# Diccionario Vacío 
d= {}

# Llave entera, valor string 
numNames = { 1:"One",2:"Two",3:"Three"}

# Llave real, valor string
decNames = { 1.5:"One and Half" , 2.5: "Two and half", 3.5: "Three and half"}

# Llave tupla, valor string
items = {("Parker","Reynolds","Camlin"):"pen", ("LG", "Whirlpool","Samsung"): "Refrigerador"}

# Llave string, valor int

romanNums = {'I':1, 'II':2, 'III':3,'IV':4, 'V':5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("india"))

# Reportar llave y valor 
for k in capitals: 
     print("Key =" + k + ",Value = " + capitals [k])

# Nuevo dato para el diccionario 
capitals ["Mexico"] = " CDMX"
print(capitals)

# Borrar dato del diccionario
del capitals ["Mexico"]
print(capitals)

# Borrar todo el diccionario
del capitals 

# Reportar llaves 
print(romanNums.keys())

# Reportar valores 
print(romanNums.values())

# Juicio de llave (está o no está la llave en el diccionario)

print("T" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)


