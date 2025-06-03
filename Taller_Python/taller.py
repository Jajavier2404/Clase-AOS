#EJERCICIOS REALIZADOS POR JAVIER ALEXANDER GOMEZ DELGADO   
def ejercicio_1():
    """
    Ejercicio 1: Suma de dos números
    Pide dos números al usuario, almacénalos en variables y muestra su suma.
    """
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es: {suma}")


def ejercicio_2():
    """
    Ejercicio 2: Conversión de grados Celsius a Fahrenheit
    Fórmula: F = C * 1.8 + 32
    """
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius} °C equivalen a {fahrenheit} °F")


def ejercicio_3():
    """
    Ejercicio 3: Área de un triángulo
    Fórmula: Área = (base * altura) / 2
    """
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")


def ejercicio_4():
    """
    Ejercicio 4: Par o impar
    Pide un número y determina si es par o impar usando if.
    """
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")


def ejercicio_5():
    """
    Ejercicio 5: Intercambiar valores entre dos variables
    Intercambia los valores de dos variables sin usar una tercera variable.
    """
    a = input("Ingrese el valor de a: ")
    b = input("Ingrese el valor de b: ")
    print(f"Antes del intercambio: a = {a}, b = {b}")
    a, b = b, a
    print(f"Después del intercambio: a = {a}, b = {b}")


def ejercicio_6():
    """
    Ejercicio 6: Calculadora simple
    Realiza suma, resta, multiplicación y división con dos números ingresados por el usuario.
    """
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Error: división por cero"

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")


def ejercicio_7():
    """
    Ejercicio 7: Edad en años, meses y días
    A partir de la edad en años, calcula la cantidad aproximada de meses y días.
    Considera 1 año = 12 meses y 1 mes = 30 días aproximadamente.
    """
    años = int(input("Ingrese su edad en años: "))
    meses = años * 12
    dias = meses * 30
    print(f"Tienes aproximadamente {meses} meses o {dias} días.")


def ejercicio_8():
    """
    Ejercicio 8: Número mayor
    Pide tres números al usuario y muestra cuál es el mayor.
    """
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3

    print(f"El número mayor es: {mayor}")


def ejercicio_9():
    """
    Ejercicio 9: Verificar si un número es múltiplo de otro
    Pide dos números y determina si el primero es múltiplo del segundo.
    """
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if num2 == 0:
        print("No se puede dividir por cero.")
    else:
        if num1 % num2 == 0:
            print(f"{num1} es múltiplo de {num2}.")
        else:
            print(f"{num1} NO es múltiplo de {num2}.")


def ejercicio_10():
    """
    Ejercicio 10: Salario con bonificación
    Calcula el salario total si un empleado recibe un bono del 10% sobre su salario base.
    """
    salario_base = float(input("Ingrese el salario base del empleado: "))
    bono = salario_base * 0.10
    salario_total = salario_base + bono
    print(f"El salario total con bonificación es: {salario_total}")


print("Seleccione el ejercicio a ejecutar (1-10):")
ejercicio = input()

if ejercicio == '1':
    ejercicio_1()
elif ejercicio == '2':
    ejercicio_2()
elif ejercicio == '3':
    ejercicio_3()
elif ejercicio == '4':
    ejercicio_4()
elif ejercicio == '5':
    ejercicio_5()
elif ejercicio == '6':
    ejercicio_6()
elif ejercicio == '7':
    ejercicio_7()
elif ejercicio == '8':
    ejercicio_8()
elif ejercicio == '9':
    ejercicio_9()
elif ejercicio == '10':
    ejercicio_10()
else:
    print("Opción no válida.")
