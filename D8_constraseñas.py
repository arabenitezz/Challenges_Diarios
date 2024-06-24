# Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable
# (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.

# Importamos random para utilizar el metodo aleatorio y string para no tener que crear listas de los caracteres permitidos manualmente
import string
import random

# Definimos la longitud de la contraseña de forma aleatoria entre 8 y 16 caracteres
password_length = random.randint(8, 16)

# Definimos caracteres posibles para la contraseña
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Combinamos todos los caracteres posibles
all_characters = letters + numbers + symbols

# Creamos la contraseña garantizando al menos un carácter de cada tipo
password = [
    random.choice(letters),
    random.choice(numbers),
    random.choice(symbols)
]

# Rellenamos el resto de la contraseña con caracteres aleatorios
password += random.choices(all_characters, k=password_length - 3)

# Mezclamos los caracteres para asegurar un orden aleatorio
random.shuffle(password)

# Convertimos la lista de caracteres en una cadena
final_password = ''.join(password)

print(f'Su contraseña es: {final_password}')


