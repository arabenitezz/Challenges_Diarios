def invertir_caracteres(cadena_De_caracteres):  # Define la función invertir_caracteres que toma una cadena como argumento.
    if len(cadena_De_caracteres) == 0:  # Verifica si la longitud de la cadena es 0.
        return ""  # Si es así, retorna una cadena vacía.
    else:  # Si la cadena no está vacía,
        return cadena_De_caracteres[-1] + invertir_caracteres(cadena_De_caracteres[:-1])  # Retorna el último carácter de la cadena más la llamada recursiva de la función con la cadena sin el último carácter.
    
# Solicita al usuario que ingrese una palabra
cadena_usuario = input("Ingrese una palabra: ")

# Llama a la función invertir_caracteres con la cadena ingresada por el usuario
resultado = invertir_caracteres(cadena_usuario)

# Imprime el resultado
print(resultado)