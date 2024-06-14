# Pedir una palabra al usuario
palabra_solicitada = input('Escribe una palabra: ')

# Definir vocales

vocales = ['a', 'e', 'i', 'o' , 'u', 'A', 'E', 'I', 'O', 'U']

# Funcion contadora de vocales
def contador_vocales (palabra_elegida):
    # Iniciar un contador en 0
    contador = 0
    for letras in palabra_elegida:
        if letras in vocales:
            contador += 1
        else:
            contador += 0
    print(f'La cantidad de vocales en tu palabra es: {contador}')

contador_vocales(palabra_solicitada)

