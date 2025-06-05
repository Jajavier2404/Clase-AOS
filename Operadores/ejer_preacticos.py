### EJERCICIOS REALIZADOS POR JAVIER ALEXANDER GOMEZ DELGADO ###
# EJERCICIOS DE OPERADORES LÓGICOS Y RELACIONALES

# 11. Expresión que devuelva True si x es mayor que 10 y menor que 20
def ejercicio_11(x):
    return x > 10 and x < 20
    # También se puede escribir como: 10 < x < 20

print("Ejercicio 11:")
print(f"x = 15: {ejercicio_11(15)}")  # True
print(f"x = 5: {ejercicio_11(5)}")    # False
print(f"x = 25: {ejercicio_11(25)}")  # False

# 12. Condición que devuelva True si a es igual a b o c es mayor que 100
def ejercicio_12(a, b, c):
    return a == b or c > 100

print("\nEjercicio 12:")
print(f"a=5, b=5, c=50: {ejercicio_12(5, 5, 50)}")    # True (a == b)
print(f"a=5, b=10, c=150: {ejercicio_12(5, 10, 150)}")  # True (c > 100)
print(f"a=5, b=10, c=50: {ejercicio_12(5, 10, 50)}")   # False

# 13. ¿Qué devuelve esta expresión y por qué? True or False and False
print("\nEjercicio 13:")
resultado_13 = True or False and False
print(f"True or False and False = {resultado_13}")
print("Explicación: El operador 'and' tiene mayor precedencia que 'or'")
print("Se evalúa como: True or (False and False) = True or False = True")

# 14. ¿Qué resultado tiene la siguiente operación? (5 > 3) ^ (2 < 1)
print("\nEjercicio 14:")
resultado_14 = (5 > 3) ^ (2 < 1)
print(f"(5 > 3) ^ (2 < 1) = {resultado_14}")
print("Explicación: True ^ False = True (XOR devuelve True cuando los valores son diferentes)")

# 15. Reescribe usando operadores relacionales y lógicos: not (a < b or b < c)
def ejercicio_15_original(a, b, c):
    return not (a < b or b < c)

def ejercicio_15_reescrita(a, b, c):
    # Aplicando leyes de De Morgan: not (A or B) = (not A) and (not B)
    return (a >= b) and (b >= c)

print("\nEjercicio 15:")
print("Expresión original: not (a < b or b < c)")
print("Expresión reescrita: (a >= b) and (b >= c)")
a, b, c = 10, 5, 3
print(f"Con a={a}, b={b}, c={c}:")
print(f"Original: {ejercicio_15_original(a, b, c)}")
print(f"Reescrita: {ejercicio_15_reescrita(a, b, c)}")

# 16. Condición que devuelva True solo si x y y son diferentes y al menos uno > 15
def ejercicio_16(x, y):
    return (x != y) and (x > 15 or y > 15)

print("\nEjercicio 16:")
print(f"x=10, y=20: {ejercicio_16(10, 20)}")  # True (diferentes y y > 15)
print(f"x=10, y=10: {ejercicio_16(10, 10)}")  # False (iguales)
print(f"x=5, y=8: {ejercicio_16(5, 8)}")      # False (diferentes pero ninguno > 15)

# 17. Evalúa: (10 != 5) and (4 == 4) or (2 > 3)
print("\nEjercicio 17:")
resultado_17 = (10 != 5) and (4 == 4) or (2 > 3)
print(f"(10 != 5) and (4 == 4) or (2 > 3) = {resultado_17}")
print("Paso a paso:")
print("(10 != 5) = True")
print("(4 == 4) = True")
print("(2 > 3) = False")
print("True and True or False = True or False = True")

# 18. Dado el código, ¿cuál es el valor de resultado?
print("\nEjercicio 18:")
a = True
b = False
resultado = a ^ b
print(f"a = {a}")
print(f"b = {b}")
print(f"resultado = a ^ b = {resultado}")
print("Explicación: True ^ False = True (XOR de valores diferentes)")

# 19. ¿Qué devuelve esta expresión? (3 > 2) and (2 > 1) ^ False
print("\nEjercicio 19:")
resultado_19 = (3 > 2) and (2 > 1) ^ False
print(f"(3 > 2) and (2 > 1) ^ False = {resultado_19}")
print("Paso a paso:")
print("(3 > 2) = True")
print("(2 > 1) = True")
print("^ tiene mayor precedencia que and")
print("Se evalúa como: True and (True ^ False) = True and True = True")

# 20. Programa que reciba dos números y diga si exactamente uno es positivo
def exactamente_uno_positivo(num1, num2):
    """
    Usa XOR para verificar si exactamente uno de los números es positivo.
    XOR devuelve True solo cuando los valores son diferentes.
    """
    es_positivo_1 = num1 > 0
    es_positivo_2 = num2 > 0
    return es_positivo_1 ^ es_positivo_2

print("\nEjercicio 20:")
print("Programa que verifica si exactamente uno de dos números es positivo:")

# Casos de prueba
casos_prueba = [
    (5, -3),   # Exactamente uno positivo
    (-2, 7),   # Exactamente uno positivo
    (4, 8),    # Ambos positivos
    (-1, -5),  # Ninguno positivo
    (0, 3),    # Uno es cero, otro positivo
    (-4, 0)    # Uno negativo, otro cero
]

for num1, num2 in casos_prueba:
    resultado = exactamente_uno_positivo(num1, num2)
    print(f"números {num1} y {num2}: {resultado}")

# Versión interactiva del ejercicio 20
def programa_interactivo():
    print("\n--- Programa Interactivo ---")
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if exactamente_uno_positivo(num1, num2):
            print("Exactamente uno de los números es positivo.")
        else:
            print("No se cumple la condición (ambos son positivos, ambos son no-positivos, o hay un cero).")
            
    except ValueError:
        print("Por favor, ingresa números válidos.")

# Descomenta la siguiente línea para ejecutar el programa interactivo
# programa_interactivo()