# Sección 2: Operadores Relacionales
# Ejercicios del 11 al 20

print("=== SECCIÓN 2: OPERADORES RELACIONALES ===\n")

# 11. Verificación de rango
print("11. Verificación de rango")
x = 55
resultado = 10 <= x <= 100
print(f"¿{x} está entre 10 y 100 (inclusive)? {resultado}\n")

# 12. Comparación de strings (ignorar mayúsculas)
print("12. Comparación de strings (ignorar mayúsculas)")
a = "Hola"
b = "HOLA"
son_iguales = a.lower() == b.lower()
print(f"'{a}' == '{b}' (ignorando mayúsculas): {son_iguales}\n")

# 13. Igualdad entre tres variables
print("13. Igualdad entre tres variables")
var1 = 5
var2 = 5
var3 = 5
todas_iguales = var1 == var2 == var3
print(f"var1={var1}, var2={var2}, var3={var3}")
print(f"¿Tienen el mismo valor? {todas_iguales}\n")

# 14. Presencia en lista
print("14. Presencia en lista")
numeros = [1, 5, 10, 15, 20, 25]
x = 15
esta_presente = x in numeros
print(f"Lista: {numeros}")
print(f"¿{x} está en la lista? {esta_presente}\n")

# 15. Divisibilidad por 3 y 5
print("15. Divisibilidad por 3 y 5")
n = 15
divisible_por_3_y_5 = n % 3 == 0 and n % 5 == 0
print(f"¿{n} es divisible por 3 y 5? {divisible_por_3_y_5}\n")

# 16. Números en orden estricto
print("16. Números en orden estricto")
a = 5
b = 10
c = 15
orden_ascendente = a < b < c
print(f"a={a}, b={b}, c={c}")
print(f"¿Están en orden ascendente estricto? {orden_ascendente}\n")

# 17. Comparación doble
print("17. Comparación doble")
x = 25
a = 20
b = 30
esta_entre = a < x < b
print(f"¿{x} está estrictamente entre {a} y {b}? {esta_entre}\n")

# 18. Relación proporcional
print("18. Relación proporcional")
a = 10
b = 5
es_doble = a == 2 * b
print(f"a={a}, b={b}")
print(f"¿a es exactamente el doble de b? {es_doble}\n")

# 19. Cambio de signo si negativo
print("19. Cambio de signo si negativo")
x = -8
print(f"Valor original: {x}")
if x < 0:
    x = -x
print(f"Valor después del cambio: {x}\n")

# 20. Detección de tipo
print("20. Detección de tipo")
variables = [42, 3.14, "texto", True]
for var in variables:
    if isinstance(var, int) and not isinstance(var, bool):  # bool es subclase de int
        tipo = "entero (int)"
    elif isinstance(var, float):
        tipo = "flotante (float)"
    elif isinstance(var, str):
        tipo = "cadena (str)"
    elif isinstance(var, bool):
        tipo = "booleano (bool)"
    else:
        tipo = "otro tipo"
    print(f"{var} es de tipo: {tipo}")