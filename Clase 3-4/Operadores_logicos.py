print("\n== Operadores Lógicos ==")

a = int(input("¿Tienes más de 18 años? (1 = Sí, 0 = No): "))
b = int(input("¿Tienes licencia de conducir? (1 = Sí, 0 = No): "))

es_mayor = bool(a)
tiene_licencia = bool(b)

print("\n== Resultados ==")
print("¿Puede conducir? (mayor de edad Y con licencia):", es_mayor and tiene_licencia)
print("¿Cumple alguna condición? (edad o licencia):", es_mayor or tiene_licencia)
print("¿No tiene licencia?:", not tiene_licencia)
