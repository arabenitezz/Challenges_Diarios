#include <iostream>
#include <string>
#include <algorithm> // Para std::equal y std::reverse
#include <cctype>    // Para std::tolower

bool esPalindromo(const std::string& palabra) {
    // Copiamos la palabra y eliminamos los espacios si es necesario
    std::string palabraSinEspacios;
    for (char c : palabra) {
        if (!std::isspace(c)) {
            palabraSinEspacios += std::tolower(c); // Convertimos a minúsculas
        }
    }

    // Creamos una copia invertida de la palabra
    std::string palabraInvertida = palabraSinEspacios;
    std::reverse(palabraInvertida.begin(), palabraInvertida.end());

    // Comparamos la palabra original con la invertida
    return std::equal(palabraSinEspacios.begin(), palabraSinEspacios.end(), palabraInvertida.begin());
}

int main() {
    std::string palabra;
    std::cout << "Ingrese una palabra para verificar si es palindromo: ";
    std::cin >> palabra;

    if (esPalindromo(palabra)) {
        std::cout << "La palabra '" << palabra << "' es un palindromo.\n";
    } else {
        std::cout << "La palabra '" << palabra << "' no es un palindromo.\n";
    }

    return 0;
}

