# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 00:06:57 2025

@author: LENOVO
"""

import random


def obtener_nombre_jugador(num):
    return input(f"Nombre del Jugador {num}: ")


nombre_jugador1 = obtener_nombre_jugador(1)
nombre_jugador2 = obtener_nombre_jugador(2)

print(f"Jugador 1: {nombre_jugador1}")
print(f"Jugador 2: {nombre_jugador2}")


estadisticas = []


conteo_victorias = {
    nombre_jugador1: 0,
    nombre_jugador2: 0,
    "Computadora": 0,
    "Empates": 0
}

def obtener_opcion():
    opciones = ['piedra', 'papel', 'tijeras']
    while True:
        opcion = input("Elige piedra, papel o tijeras: ").lower()
        if opcion in opciones:
            return opcion
        print("Opción no válida. Intenta de nuevo.")

def determinar_ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == "piedra" and opcion2 == "tijeras") or \
         (opcion1 == "papel" and opcion2 == "piedra") or \
         (opcion1 == "tijeras" and opcion2 == "papel"):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"


def jugar_contra_computadora():
    usuario = obtener_opcion()
    computadora = random.choice(["piedra", "papel", "tijeras"])
    print(f"Computadora eligió: {computadora}")
    resultado = determinar_ganador(usuario, computadora)

    if resultado == "Empate":
        conteo_victorias["Empates"] += 1
    elif resultado == "Jugador 1 gana":
        conteo_victorias[nombre_jugador1] += 1
    else:
        conteo_victorias["Computadora"] += 1

    print(f"Resultado: {resultado}")

 
    estadisticas.append((nombre_jugador1, "Computadora", usuario, computadora, resultado))


def jugar_multijugador():
    print(f"{nombre_jugador1}, ingresa tu opción (no se mostrará en pantalla)")
    opcion1 = obtener_opcion()
    print("\n" * 50)  
    print(f"{nombre_jugador2}, ingresa tu opción (no se mostrará en pantalla)")
    opcion2 = obtener_opcion()
    print("\n" * 50)

    resultado = determinar_ganador(opcion1, opcion2)

    if resultado == "Empate":
        conteo_victorias["Empates"] += 1
    elif resultado == "Jugador 1 gana":
        conteo_victorias[nombre_jugador1] += 1
    else:
        conteo_victorias[nombre_jugador2] += 1

    print(f"Resultado: {resultado}")

    
    estadisticas.append((nombre_jugador1, nombre_jugador2, opcion1, opcion2, resultado))


def mostrar_estadisticas():
    total_partidas = len(estadisticas)
    if total_partidas == 0:
        print("No hay estadísticas aún.")
    else:
        print(f"\nTotal de partidas jugadas: {total_partidas}")
        print("\nÚltimas partidas:")
        for i, (j1, j2, o1, o2, res) in enumerate(estadisticas[-5:], 1):  # Mostrar solo las últimas 5
            print(f"{i}. {j1} ({o1}) vs {j2} ({o2}) -> {res}")

        print("\nConteo de victorias:")
        for jugador, victorias in conteo_victorias.items():
            print(f"{jugador}: {victorias} victorias")


def mostrar_ultima_partida():
    if estadisticas:
        j1, j2, o1, o2, res = estadisticas[-1]
        print("\n--- Última partida ---")
        print(f"{j1} ({o1}) vs {j2} ({o2}) -> {res}")
    else:
        print("Aún no se ha jugado ninguna partida.")


def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar contra la computadora")
        print("2. Modo multijugador")
        print("3. Ver estadísticas de las últimas 5 partidas y conteo de victorias")
        print("4. Ver la última partida")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            jugar_contra_computadora()
        elif opcion == "2":
            jugar_multijugador()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            mostrar_ultima_partida()
        elif opcion == "5":
            print("Saliendo del juego...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


menu()