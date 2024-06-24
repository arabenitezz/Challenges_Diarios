# Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o
# tijeras contra la computadora.

# Importar random de la libreria python
import random

# Pedir al usuario que elija una opcion

movimiento_usuario = str(input('Piedra, papel o tijera?: ')).lower()

# Definir movimientos posibles del usuario y la computadora

movimientos_posibles = ['piedra', 'papel', 'tijera']

# Hacer los movimientos de la computadora random

movimiento_computadora = random.choice(movimientos_posibles)

# Crear la funcion del juego

def juego ():

    if movimiento_usuario not in movimientos_posibles:
        print('Ingrese una opcion valida')
    else:
        print(f'La computadora ha elegido {movimiento_computadora}')

# Crear una funcion que verifique al ganador

def verificar_ganador ():

    if movimiento_usuario == movimiento_computadora:
        print('Es un empate!')

    elif movimiento_usuario == 'piedra' and movimiento_computadora == 'tijera' or movimiento_usuario == 'papel' and movimiento_computadora == 'piedra' or movimiento_usuario == 'tijera' and movimiento_computadora == 'papel':
        print('Has ganado!')
    else:
        print('Has perdido!')

juego()
verificar_ganador()
