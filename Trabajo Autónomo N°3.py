# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:05:21 2025

@author: LENOVO
"""

import random

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
    global estadisticas
    usuario = obtener_opcion()
    computadora = random.choice(["piedra", "papel", "tijeras"])
    print(f"Computadora eligió: {computadora}")
    resultado = determinar_ganador(usuario, computadora)
    print(f"Resultado: {resultado}")
    estadisticas.append((usuario, computadora, resultado))

def jugar_multijugador():
    global estadisticas
    print("Jugador 1, ingresa tu opción (no se mostrará en pantalla)")
    opcion1 = obtener_opcion()
    print("\n" * 50)  # Simulación de limpiar pantalla
    print("Jugador 2, ingresa tu opción (no se mostrará en pantalla)")
    opcion2 = obtener_opcion()
    print("\n" * 50)
    resultado = determinar_ganador(opcion1, opcion2)
    print(f"Resultado: {resultado}")
    estadisticas.append((opcion1, opcion2, resultado))

def mostrar_estadisticas():
    if not estadisticas:
        print("No hay estadísticas aún.")
    else:
        print("Últimas partidas:")
        for i, (p1, p2, res) in enumerate(estadisticas[-5:], 1):  # Últimas 5 partidas
            print(f"{i}. Jugador 1: {p1} - Jugador 2: {p2} -> {res}")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar contra la computadora")
        print("2. Modo multijugador")
        print("3. Ver estadísticas de la última partida")
        print("4. Regresar al menú principal")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            jugar_contra_computadora()
        elif opcion == "2":
            jugar_multijugador()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida, intenta de nuevo.")

estadisticas = []
menu()