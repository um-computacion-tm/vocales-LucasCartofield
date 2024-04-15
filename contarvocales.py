import unittest


def contar_vocales(palabra):
    vocales = ("a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú")
    resultado = {}
    for letra in palabra.lower(): # Convierte las letras en palabra a minúscula
        if letra in vocales:
            # La letra es vocal
            if letra in resultado.keys():
                # Sumar valor a diccionario ya existente
                resultado[letra] += 1
            else:
                # Agregar letra por primera vez
                resultado[letra] = 1

    return resultado

if __name__ == '__main__':
    unittest.main()

