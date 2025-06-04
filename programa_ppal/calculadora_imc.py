# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'funciones')))
import funciones as func

imc = func.calcular_imc( 
        func.ingresar_numero_flotante("Ingrese su peso en Kg: ", 0.1), 
        func.ingresar_numero_flotante("Ingrese su altura en metros: ", 0.01) )

print(f"\nEl índice de masa corporal (IMC) es: {imc:.2f}\n")