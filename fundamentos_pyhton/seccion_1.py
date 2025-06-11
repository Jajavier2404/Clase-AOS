### EJERCICIOS REALIZADOS POR JAVIER ALEXANDER GOMEZ DELGADO ###

# Sección 1: Variables
# Ejercicios del 1 al 10

print("=== SECCIÓN 1: VARIABLES ===\n")

# 1. Intercambio sin variable auxiliar
print("1. Intercambio sin variable auxiliar")
a = 10
b = 20
print(f"Antes: a = {a}, b = {b}")
a, b = b, a
print(f"Después: a = {a}, b = {b}\n")

# 2. Suma de cuadrados
print("2. Suma de cuadrados")
a = 5
b = 3
c = a**2 + b**2
print(f"a = {a}, b = {b}")
print(f"a² + b² = {a}² + {b}² = {c}\n")

# 3. Conversión de tipos
print("3. Conversión de tipos")
numero = 42
print(f"Entero original: {numero} (tipo: {type(numero)})")
numero_str = str(numero)
print(f"A string: {numero_str} (tipo: {type(numero_str)})")
numero_float = float(numero_str)
print(f"A float: {numero_float} (tipo: {type(numero_float)})")
numero_int = int(numero_float)
print(f"A int nuevamente: {numero_int} (tipo: {type(numero_int)})\n")

# 4. Redondeo y formato
print("4. Redondeo y formato")
numero = 17.8567
redondeado = round(numero, 2)
resultado = f"Resultado: {redondeado}"
print(resultado)
print(f"Tipo del resultado: {type(resultado)}\n")

# 5. Concatenación de variables
print("5. Concatenación de variables")
nombre = "Juan"
edad = 25
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje + "\n")

# 6. Cálculo de edad actual
print("6. Cálculo de edad actual")
anio_actual = 2025
anio_nacimiento = 1995
edad_actual = anio_actual - anio_nacimiento
print(f"Año actual: {anio_actual}")
print(f"Año de nacimiento: {anio_nacimiento}")
print(f"Edad actual: {edad_actual} años\n")

# 7. Cuenta regresiva con variables
print("7. Cuenta regresiva con variables")
contador = 10
while contador >= 0:
    print(contador)
    contador -= 1
print()

# 8. Valor absoluto sin usar abs()
print("8. Valor absoluto sin usar abs()")
numero = -15
if numero < 0:
    valor_absoluto = -numero
else:
    valor_absoluto = numero
print(f"Número: {numero}")
print(f"Valor absoluto: {valor_absoluto}\n")

# 9. Incremento/decremento según paridad
print("9. Incremento/decremento según paridad")
n = 7
print(f"Número original: {n}")
if n % 2 == 0:  # Es par
    n += 1
    print(f"Era par, se sumó 1: {n}")
else:  # Es impar
    n -= 1
    print(f"Era impar, se restó 1: {n}")
print()

# 10. Máximo entre tres números
print("10. Máximo entre tres números")
a = 15
b = 8
c = 23
print(f"a = {a}, b = {b}, c = {c}")

if a >= b and a >= c:
    maximo = a
elif b >= a and b >= c:
    maximo = b
else:
    maximo = c

print(f"El mayor es: {maximo}")