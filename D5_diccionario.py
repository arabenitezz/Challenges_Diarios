# Challenge ---> Crear un Diccionario: Escribe un programa que cree un diccionario a partir de
# dos listas dadas: una de claves y otra de valores.

# Listas dadas
claves = ["matematica", "fisica", "calculo", "geometria"]
valores = ["5", "3", "4", "5"]

# Creamos el diccionario

calificaciones = dict(zip(claves, valores))

# zip: La función zip combina las dos listas, emparejando cada clave con su valor correspondiente.
# dict: La función dict convierte el resultado de zip en un diccionario.

#Imprimimos el resultado
print(calificaciones)