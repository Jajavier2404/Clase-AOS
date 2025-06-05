# Sección 3: Operadores Lógicos
# Ejercicios del 21 al 30

print("=== SECCIÓN 3: OPERADORES LÓGICOS ===\n")

# 21. ¿Puede votar?
print("21. ¿Puede votar?")
edad = 20
tiene_documento = True
puede_votar = edad >= 18 and tiene_documento
print(f"Edad: {edad}, Tiene documento: {tiene_documento}")
print(f"¿Puede votar? {puede_votar}\n")

# 22. Control de acceso lógico
print("22. Control de acceso lógico")
tiene_pase_vip = False
paga_entrada = True
esta_ebrio = False
puede_entrar = tiene_pase_vip or (paga_entrada and not esta_ebrio)
print(f"Pase VIP: {tiene_pase_vip}, Paga entrada: {paga_entrada}, Está ebrío: {esta_ebrio}")
print(f"¿Puede entrar? {puede_entrar}\n")

# 23. Validación XOR
print("23. Validación XOR")
cond1 = True
cond2 = False
xor_resultado = (cond1 and not cond2) or (not cond1 and cond2)
# También se puede usar: xor_resultado = cond1 != cond2
print(f"Condición 1: {cond1}, Condición 2: {cond2}")
print(f"XOR (exactamente una es verdadera): {xor_resultado}\n")

# 24. Validación compuesta múltiple
print("24. Validación compuesta múltiple")
n = 6
condicion = n > 0 and (n % 2 == 0 or n % 3 == 0)
print(f"Número: {n}")
print(f"¿Es mayor que 0 y (múltiplo de 2 o de 3)? {condicion}\n")

# 25. Condición contradictoria
print("25. Condición contradictoria")
x = 10
contradiccion = x > 5 and x < 1
print(f"x = {x}")
print(f"¿x > 5 AND x < 1? {contradiccion} (siempre False)\n")

# 26. Negación lógica
print("26. Negación lógica")
x = 15
# Condición original: x > 10
# Negación equivalente: not (x > 10) = x <= 10
condicion_original = x > 10
condicion_negada = not (x > 10)
condicion_equivalente = x <= 10
print(f"x = {x}")
print(f"x > 10: {condicion_original}")
print(f"not (x > 10): {condicion_negada}")
print(f"x <= 10: {condicion_equivalente}\n")

# 27. Aprobación de estudiante
print("27. Aprobación de estudiante")
nota = 3.5
asistencia = 85
aprueba = nota >= 3.0 and asistencia >= 80
print(f"Nota: {nota}, Asistencia: {asistencia}%")
print(f"¿Aprueba? {aprueba}\n")

# 28. Simulación de alarma
print("28. Simulación de alarma")
temperatura = 40
humedad = 85
alarma = (temperatura < 0 or temperatura > 38) and humedad > 80
print(f"Temperatura: {temperatura}°C, Humedad: {humedad}%")
print(f"¿Se activa la alarma? {alarma}\n")

# 29. Contraseña segura
print("29. Contraseña segura")
password = "mipassword123"
longitud_ok = len(password) > 8
tiene_numero = any(char.isdigit() for char in password)
es_segura = longitud_ok and tiene_numero
print(f"Contraseña: '{password}'")
print(f"Longitud > 8: {longitud_ok}")
print(f"Tiene números: {tiene_numero}")
print(f"¿Es segura? {es_segura}\n")

# 30. Doble negación lógica
print("30. Doble negación lógica")
tiene_acceso = True
# "No es falso que no tenga acceso" = not (not tiene_acceso) = tiene_acceso
expresion = not (not tiene_acceso)
print(f"Tiene acceso: {tiene_acceso}")
print(f"'No es falso que no tenga acceso': {expresion}")
print(f"Equivale a: {expresion == tiene_acceso}")